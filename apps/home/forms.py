from django import forms
from apps.home.models import Contact, Gallery, Feedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = "__all__"

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ("name", "title_or_position", "company_name", "image", "feedback_message",)
