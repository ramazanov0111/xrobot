from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    ###Категории###
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("service_list", kwargs={"category_url": self.url})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Service(models.Model):
    ###Услуги###
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="services/")
    price = models.PositiveSmallIntegerField("Цена", default=0, help_text="указывать цену в рублях")
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Order(models.Model):
    ###Заявки###
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    phone = models.CharField("Телефон", max_length=12)
    site = models.CharField("Адрес сайта", max_length=50)
    image = models.ImageField("Файл", upload_to="orders/")
    service = models.ForeignKey(
        Service, verbose_name="Услуга", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} - {self.service}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Reviews(models.Model):
    ###Отзывы###
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField()
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.service}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
