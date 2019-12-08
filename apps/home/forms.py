from django import forms
from apps.home.models import Contact, Gallery


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"