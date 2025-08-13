from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Book, Author, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'authors', 'category', 'price', 'rent_price']
        widgets = {
            'publication_date': forms.SelectDateWidget(years=range(1700, timezone.now().year + 1)),
            'authors': forms.CheckboxSelectMultiple(),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title or len(title) < 3:
            raise ValidationError('Title must be at least 3 characters long.')
        return title

    def clean_publication_date(self):
        pub_date = self.cleaned_data.get('publication_date')
        if pub_date > timezone.now().date():
            raise ValidationError('Publication date cannot be in the future.')
        return pub_date

class RentOrBuyForm(forms.Form):
    CHOICES = (
        ('buy', 'Buy'),
        ('rent', 'Rent')
    )
    action = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    payment_method = forms.ChoiceField(choices=[('netbanking', 'Netbanking'), ('cash', 'Cash')], widget=forms.RadioSelect)

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=6, decimal_places=2)
    payment_method = forms.CharField(max_length=100)
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError('Name is required.')
        return name

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        msg = self.cleaned_data.get('message')
        if len(msg.split()) < 5:
            raise ValidationError('Message must contain at least 5 words.')
        return msg