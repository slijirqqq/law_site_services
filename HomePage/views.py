from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View

from .forms import ContactForm, ReviewForm, QuestionForm
from .models import SiteInfo, PartnerModel, EmployeeModel, Reviews, Practice_areas, AboutPageModel, SertificatesModel, \
    Questions


def Site_info():
    return SiteInfo.objects.get(pk=1)


def About_page_model():
    return AboutPageModel.objects.all()


class ContactView(View):
    template_name = 'HomePage/contact.html'
    context = {'site_info': Site_info(), 'services': Practice_areas.objects.all()}

    def get(self, request):
        self.context['form'] = ContactForm()
        self.context['question_form'] = QuestionForm()
        return render(request, self.template_name, self.context)

    def post(self, request):
        if 'sub' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                phone_number = form.cleaned_data['phone_number']
                sender = form.cleaned_data['sender']
                form.save(commit=True)
                subject = f'Сообщение с формы от {sender}'
                recipients = ['cult6.cult6.cult6@gmail.com']
                try:
                    send_mail(subject, message + '\n' + str(phone_number), sender, recipients)
                except BadHeaderError:  # Защита от уязвимости
                    return HttpResponse('Invalid header found')
                context = {'message': 'Спасибо за вашу заявку, скоро мы ответим!',
                           'site_info': Site_info(),
                           'services': Practice_areas.objects.all()}
                return render(request, 'HomePage/thanks.html', context)
            self.context['form'] = form
            self.context['question_form'] = QuestionForm()
            return render(request, self.template_name, self.context)
        if 'quest' in request.POST:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question_text = question_form.cleaned_data['question_text']
                question_form.save(commit=True)
                context = {'message': 'Спасибо за оставленный вами вопрос, скоро мы на него ответим!',
                           'site_info': Site_info(), 'services': Practice_areas.objects.all()}
                return render(request, 'HomePage/thanks.html', context)
            self.context['form'] = ContactForm()
            self.context['question_form'] = question_form
            return render(request, self.template_name, self.context)


class ServiceDetail(View):
    template_name = 'HomePage/service-detail.html'
    context = {'reviews': Reviews.objects.filter(created_date__lte=timezone.now()).filter(validation='y').order_by(
        "created_date").reverse()[:3], 'questions': Questions.objects.filter(answers__validation='y')[:3],
               'site_info': Site_info(), 'services': Practice_areas.objects.all()}

    def get(self, request, pk):
        self.context['service'] = Practice_areas.objects.get(pk=pk)
        self.context['form'] = ContactForm()
        self.context['question_form'] = QuestionForm()

        return render(request, 'HomePage/service-detail.html', self.context)

    def post(self, request, pk):
        if 'sub' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                phone_number = form.cleaned_data['phone_number']
                sender = form.cleaned_data['sender']
                form.save(commit=True)
                subject = f'Сообщение с формы от {sender}'
                recipients = ['cult6.cult6.cult6@gmail.com']
                try:
                    send_mail(subject, message + '\n' + str(phone_number), sender, recipients)
                except BadHeaderError:  # Защита от уязвимости
                    return HttpResponse('Invalid header found')
                context = {'message': 'Спасибо за вашу заявку, скоро мы ответим!', 'site_info': Site_info(),
                           'services': Practice_areas.objects.all()}
                return render(request, 'HomePage/thanks.html', context)
            self.context['form'] = form
            self.context['service'] = Practice_areas.objects.get(pk=pk)
            self.context['question_form'] = QuestionForm()
            return render(request, self.template_name, self.context)
        if 'quest' in request.POST:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question_text = question_form.cleaned_data['question_text']
                question_form.save(commit=True)
                context = {'message': 'Спасибо за оставленный вами вопрос, скоро мы на него ответим!',
                           'site_info': Site_info(), 'services': Practice_areas.objects.all()}
                return render(request, 'HomePage/thanks.html', context)
            self.context['form'] = ContactForm()
            self.context['service'] = Practice_areas.objects.all()
            self.context['question_form'] = question_form
            return render(request, self.template_name, self.context)


class ServicesListView(View):
    template_name = 'HomePage/services.html'
    context = {'site_info': Site_info(),
               'reviews': Reviews.objects.filter(created_date__lte=timezone.now()).filter(validation='y').order_by(
                   "created_date").reverse()[:3], 'services': Practice_areas.objects.all(),
               'questions': Questions.objects.filter(answers__validation='y')[:3]}

    def get(self, request):
        self.context['form'] = ContactForm()
        self.context['question_form'] = QuestionForm()

        return render(request, self.template_name, self.context)

    def post(self, request):
        if 'sub' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                phone_number = form.cleaned_data['phone_number']
                sender = form.cleaned_data['sender']
                form.save(commit=True)
                subject = f'Сообщение с формы от {sender}'
                recipients = ['cult6.cult6.cult6@gmail.com']
                try:
                    send_mail(subject, message + '\n' + str(phone_number), sender, recipients)
                except BadHeaderError:  # Защита от уязвимости
                    return HttpResponse('Invalid header found')
                context = {'message': 'Спасибо за вашу заявку, скоро мы ответим!', 'site_info': Site_info(),
                           'services': Practice_areas.objects.all()}
                return render(request, 'HomePage/thanks.html', context)
            self.context['form'] = form
            self.context['question_form'] = QuestionForm()
            return render(request, self.template_name, self.context)
        if 'quest' in request.POST:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question_text = question_form.cleaned_data['question_text']
                question_form.save(commit=True)
                context = {'message': 'Спасибо за оставленный вами вопрос, скоро мы на него ответим!',
                           'site_info': Site_info(), 'services': Practice_areas.objects.all()}
                return render(request, 'HomePage/thanks.html', context)
            self.context['form'] = ContactForm()
            self.context['question_form'] = question_form
            return render(request, self.template_name, self.context)


class AboutListView(View):
    template_name = 'HomePage/about.html'
    context = {'site_info': Site_info(), 'employees': EmployeeModel.objects.all(),
               'sertificates': SertificatesModel.objects.all(),
               'about': About_page_model(), 'services': Practice_areas.objects.all()}

    def get(self, request):
        self.context['form'] = ContactForm()
        return render(request, self.template_name, self.context)

    def post(self, request):
        if request.method == 'POST' and 'sub' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                phone_number = form.cleaned_data['phone_number']
                sender = form.cleaned_data['sender']
                form.save(commit=True)
                subject = f'Сообщение с формы от {sender}'
                recipients = ['cult6.cult6.cult6@gmail.com']
                try:
                    send_mail(subject, message + '\n' + str(phone_number), sender, recipients)
                except BadHeaderError:  # Защита от уязвимости
                    return HttpResponse('Invalid header found')
                context = {'message': 'Спасибо за вашу заявку, скоро мы ответим!', 'site_info': Site_info(),
                           'services': Practice_areas.objects.all()}
                return render(request, 'HomePage/thanks.html', context)
            self.context['form'] = form
            return render(request, self.template_name, self.context)


def home_page_view(request):
    site_info = Site_info()
    partners = PartnerModel.objects.all()
    employees = EmployeeModel.objects.all()
    reviews = Reviews.objects.filter(created_date__lte=timezone.now()).filter(validation='y').order_by(
        "created_date").reverse()[:4]
    practice_areas = Practice_areas.objects.all()

    if request.method == 'POST' and 'sub' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            phone_number = form.cleaned_data['phone_number']
            sender = form.cleaned_data['sender']
            form.save(commit=True)
            subject = f'Сообщение с формы от {sender}'
            recipients = ['cult6.cult6.cult6@gmail.com']
            try:
                send_mail(subject, message + '\n' + str(phone_number), sender, recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            context = {'message': 'Спасибо за вашу заявку, скоро мы ответим!', 'site_info': site_info(),
                       'services': Practice_areas.objects.all()}
            return render(request, 'HomePage/thanks.html', context)
    else:
        form = ContactForm()
    if request.method == 'POST' and 'edit' in request.POST:
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            first_name = review_form.cleaned_data['first_name']
            last_name = review_form.cleaned_data['last_name']
            text = review_form.cleaned_data['text']
            review_form.save(commit=True)
            context = {'message': 'Спасибо. Мы благодарны Вам за оставленный отзыв!',
                       'site_info': site_info(), 'services': Practice_areas.objects.all()}
            return render(request, 'HomePage/thanks.html', context)
    else:
        review_form = ReviewForm()
    return render(request, 'HomePage/home.html',
                  {'site_info': site_info(), 'partners': partners, 'employees': employees, 'form': form,
                   'reviews': reviews, 'review_form': review_form, 'practice_areas': practice_areas})
