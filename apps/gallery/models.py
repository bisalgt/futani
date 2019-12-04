from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Gallery(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="gallery")
    upload_date = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallerys")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Gallery_detail", kwargs={"pk": self.pk})

