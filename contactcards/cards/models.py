from django.db import models
from django.urls import reverse

# Create your models here.
class ContactCards(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя', blank=False, )
    surname = models.CharField(max_length=30, verbose_name='Фамилия', blank=False, )
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', blank=False)
    date_born = models.TextField(verbose_name='Дата рождения', blank=True, default='')
    phone_number = models.CharField(max_length=15, verbose_name='Телефон', blank=True, default="", )
    position = models.TextField(verbose_name='Должность', blank=True, default="", )
    address = models.CharField(max_length=100, verbose_name='Адрес проживания', blank=True, default="", )
    hobbies = models.TextField(verbose_name='Хобби', blank=True, default="", )
    add_info = models.TextField(max_length=1000, verbose_name="Дополнительная информация", default="", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info_contact', kwargs={'contact_id': self.pk})

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['name']
