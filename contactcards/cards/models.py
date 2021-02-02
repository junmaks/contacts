from django.db import models
from django.urls import reverse


# Create your models here.
class OrganizationModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название организации', blank=False)
    address = models.CharField(max_length=30, verbose_name='Юридический адрес', blank=False)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('info_contact', kwargs={'contact_id': self.pk})

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']


class ContactCards(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя', blank=False, )
    surname = models.CharField(max_length=30, verbose_name='Фамилия', blank=False, )
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', blank=False)
    date_born = models.TextField(verbose_name='Дата рождения', blank=True, default='')
    employer = models.ForeignKey('OrganizationModel', on_delete=models.PROTECT, verbose_name='Организация', blank=False, )
    position = models.TextField(verbose_name='Должность', blank=True, default="", )
    address = models.CharField(max_length=100, verbose_name='Адрес проживания', blank=True, default="", )
    hobbies = models.TextField(verbose_name='Хобби', blank=True, default="", )
    add_info = models.TextField(max_length=1000, verbose_name="Дополнительная информация", default="", blank=True)
    # employer = models.ForeignKey('OrganizationModel', on_delete=models.PROTECT, verbose_name='Организация')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info_contact', kwargs={'contact_id': self.pk})

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['name']


class PhoneNumberModel(models.Model):
    # id_phone_num = models.Field(primary_key=True, verbose_name='id_phone')
    id_user = models.ForeignKey('ContactCards', verbose_name='id_user', on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)

    def __str__(self):
        return self.phone_number

    # def get_absolute_url(self):
    #     return reverse('info_contact', kwargs={'contact_id': self.pk})

    class Meta:
        verbose_name = 'Номер телефона сотрудника'
        verbose_name_plural = 'Номера телефонов сотрудников'
        ordering = ['phone_number']
