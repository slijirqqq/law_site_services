from django.db import models
from django.urls import reverse
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from phonenumber_field.modelfields import PhoneNumberField


class ContactModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    phone_number = PhoneNumberField(null=False, blank=False, unique=False, verbose_name='Контактный телефон')
    sender = models.EmailField(verbose_name='Почта')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.sender

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class SiteInfo(models.Model):
    site_logo = ThumbnailerImageField(upload_to='images/', verbose_name='Логотип сайта')
    favicon = ThumbnailerImageField(upload_to='images/', verbose_name='Логотип сайта во вкладке')
    name = models.CharField(max_length=20, verbose_name='Название компании')
    vk_url = models.URLField(verbose_name='Ссылка на вк')
    whatsapp_url = models.URLField(verbose_name='Ссылка на whatsapp')
    telegram_url = models.URLField(verbose_name='Ссылка на telegram')
    instagram_url = models.URLField(verbose_name='Ссылка на instagram')
    email = models.EmailField(verbose_name='Почта сайта')
    phone_number = PhoneNumberField(default='89120157067', null=False, blank=False, unique=False,
                                    verbose_name='Контактный телефон')

    def __str__(self):
        return 'Компания {}'.format(self.name)

    class Meta:
        verbose_name = 'Контент сайта'
        verbose_name_plural = 'Контент сайта'


class PartnerModel(models.Model):
    partner_name = models.CharField(max_length=20, verbose_name='Название компании')
    partner_url = models.URLField(verbose_name='ссылка на сайт компании')
    partner_logo = ThumbnailerImageField(upload_to='partner_logo/', verbose_name='Лого компании')

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = 'Компания-клиент'
        verbose_name_plural = 'Компании-клиенты'


class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=20, verbose_name='Отчество', blank=True)
    specialization = models.CharField(max_length=40, verbose_name='Специализация')
    about = models.CharField(max_length=300, verbose_name='О сотруднике')
    employee_image = ThumbnailerImageField(upload_to='employees_images/',
                                           verbose_name="Фото", resize_source=dict(quality=95,
                                                                                   size=(300, 320)))
    vk_url = models.URLField(verbose_name='ссылка на вк', blank=True)
    whatsapp_url = models.URLField(verbose_name='ссылка на whatsapp', blank=True)
    telegram_url = models.URLField(verbose_name='ссылка на telegram', blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.last_name, self.first_name, self.middle_name)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Reviews(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    VALIDATION_STATUS = (
        ('y', 'Да'),
        ('n', 'Нет')
    )
    validation = models.CharField(max_length=1, choices=VALIDATION_STATUS, blank=True, default='n')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('Review-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Practice_areas(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название услуги')
    preview_text = models.CharField(max_length=400, verbose_name='Текст описания')
    overview_text = models.TextField(verbose_name='Полный текст описания')
    preview_image = ThumbnailerImageField(upload_to='practice_image/preview/',
                                          verbose_name="Превью услуги", resize_source=dict(quality=95,
                                                                                           size=(100, 100)))
    overview_image = ThumbnailerImageField(upload_to='practice_image/', verbose_name='Фото для детального описания',
                                           resize_source=dict(quality=95, size=(1000, 650)))

    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2,
                                verbose_name='Цена', null=True)

    def __str__(self):
        return 'Услуга: {}, Цена: {}'.format(self.title, self.price)

    def get_absolute_url(self):
        return reverse('Practice-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class AboutPageModel(models.Model):
    preview_image = ThumbnailerImageField(upload_to='images/', verbose_name='Фото для превью страницы О нас',
                                          resize_source=dict(quality=95, size=(1200, 1200)))
    second_preview_image = ThumbnailerImageField(upload_to='images/', verbose_name='Фото для превью страницы О нас 2',
                                                 resize_source=dict(quality=95, size=(1200, 1900)))
    our_mission = models.CharField(max_length=200, verbose_name='Наша миссия')
    our_vision = models.CharField(max_length=200, verbose_name='Наше видиние')
    our_value = models.CharField(max_length=200, verbose_name='Наща ценность')

    professional_employees = models.IntegerField(verbose_name='Количество профессиональных юристов')
    succses_areas = models.IntegerField(verbose_name='Количество успешных дел')
    clients_work = models.IntegerField(verbose_name='Клиентов в работе')
    consultation_price = models.IntegerField(verbose_name='Цена консультации', default=0)

    def __str__(self):
        return 'Информация страницы О нас'

    class Meta:
        verbose_name = 'Информация страницы О нас'
        verbose_name_plural = 'Информация страницы О нас'


class SertificatesModel(models.Model):
    id_about_page_model = models.ForeignKey(AboutPageModel, on_delete=models.CASCADE)
    sertificat_image = ThumbnailerImageField(upload_to='images/', verbose_name='Сертификат',
                                             resize_source=dict(quality=95, size=(1200, 1200)))

    def __str__(self):
        return '{} сертификат'.format(self.id)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'


class Questions(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200, verbose_name='Текст ответа')
    pub_date = models.DateTimeField(verbose_name='Дата ответа', default=timezone.now)
    VALIDATION_STATUS = (
        ('y', 'Да'),
        ('n', 'Нет')
    )
    validation = models.CharField(max_length=1, verbose_name='Валидация', default='n', choices=VALIDATION_STATUS)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
