from django.db import models
from django.utils.translation import gettext_lazy as _

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    image = models.ImageField(upload_to="gallery")
    upload_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('upload_date', '-title',)
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.email


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    title_or_position = models.CharField(max_length=255, verbose_name="Title or Position")
    company_name = models.CharField(max_length=255, verbose_name="Company Name")
    image = models.ImageField(upload_to="cutomer_images")
    feedback_message = models.TextField()
    feedback_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")
        ordering = ("feedback_date",)

    def __str__(self):
        return self.name