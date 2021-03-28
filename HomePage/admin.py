from django.contrib import admin

from .models import ContactModel, SiteInfo, PartnerModel, EmployeeModel, Reviews, Practice_areas, AboutPageModel, \
    SertificatesModel, Questions, Answers


# admin.site.register(ContactModel, name='Обратная связь')
# admin.site.register(SiteInfo, name='Контент сайта')
# admin.site.register(PartnerModel, name='Партнеры')
# admin.site.register(EmployeeModel, name='Сотрудники')
# admin.site.register(Reviews, name='Рецензенты')

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['__str__']
    fieldsets = (
        ('Контент картинок', {
            'fields': ('site_logo', 'favicon')
        }),
        ('Контактная информация', {
            'fields': ('name', 'email', 'phone_number')
        }),
        ('Ссылки на соц. сети', {
            'fields': ('vk_url', 'instagram_url', 'whatsapp_url', 'telegram_url')
        })
    )


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['__str__', 'name', 'phone_number']
    fieldsets = (
        ('Контактная информация', {
            'fields': ('sender', 'phone_number')
        }),
        ('Текст обращения', {
            'fields': ('name', 'message')
        })
    )


@admin.register(PartnerModel)
class PartnerAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['__str__', 'partner_url']
    fields = ['partner_logo', 'partner_name', 'partner_url']


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['__str__', 'specialization']
    fieldsets = (
        ('Сотрудник', {
            'fields': ('last_name', 'first_name', 'middle_name', 'employee_image')
        }),
        ('Информация о сотруднике', {
            'fields': ('specialization', 'about')
        }),
        ('Ссылки на соц. сети', {
            'fields': ('vk_url', 'whatsapp_url', 'telegram_url')
        })
    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['__str__', 'created_date']
    fieldsets = (
        ('Рецинзент', {
            'fields': ('last_name', 'first_name')
        }),
        ('Отзыв', {
            'fields': ('text', 'created_date', 'validation')
        })
    )


@admin.register(Practice_areas)
class PracticeAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['__str__']
    fieldsets = (
        ('Превью услуги', {
            'fields': ('title', 'preview_image', 'preview_text')
        }),
        ('Полное описание услуги', {
            'fields': ('overview_text', 'price', 'overview_image')
        })
    )


class SertificatesInstanceInline(admin.TabularInline):
    model = SertificatesModel


@admin.register(AboutPageModel)
class AboutPageAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['__str__']
    fieldsets = (
        ('Фото контент', {
            'fields': ('preview_image', 'second_preview_image')
        }),
        ('Миссия, видиние и ценность комании', {
            'fields': ('our_mission', 'our_vision', 'our_value')
        }),
        ('Текущая сатистика компании', {
            'fields': ('professional_employees', 'clients_work', 'succses_areas', 'consultation_price')
        })
    )
    inlines = [SertificatesInstanceInline]


class AnswerInline(admin.TabularInline):
    extra = 1
    model = Answers


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    empty_value_display = '???'
    list_display = ['question_text', 'pub_date']
    fieldsets = (
        ('Вопрос', {
            'fields': ('question_text', 'pub_date')
        }),
    )
    inlines = [AnswerInline]


admin.site.site_title = 'LAWBOX'
admin.site.site_header = 'LAWBOX'
