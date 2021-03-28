from crispy_forms.helper import FormHelper
from django import forms
from django.forms import Textarea

from .models import ContactModel, Reviews, Questions


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = {'name', 'phone_number', 'sender', 'message'}
        widgets = {
            'name': Textarea(
                attrs={'placeholder': 'Напишите свое имя',
                       'rows': 1
                       }
            ),
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение',
                    'rows': 5
                }
            ),
            'sender': Textarea(
                attrs={
                    'placeholder': 'Напишите почту',
                    'rows': 1
                }
            ),
            'phone_number': Textarea(
                attrs={
                    'placeholder': 'Напишите контактный телефон',
                    'rows': 1
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = {'first_name', 'last_name', 'text'}
        widgets = {
            'text': Textarea(
                attrs={
                    'placeholder': 'Напишите свой отзыв',
                    'rows': 3
                }
            ),
            'first_name': Textarea(
                attrs={
                    'placeholder': 'Напишите имя',
                    'rows': 1
                }
            ),
            'last_name': Textarea(
                attrs={
                    'placeholder': 'Напишите фамилию',
                    'rows': 1
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = {'question_text', }
        widgets = {
            'question_text': Textarea(
                attrs={
                    'placeholder': 'Какой у вас вопрос?',
                    'rows': 1,
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
