from django.views.generic.edit \
        import CreateView, UpdateView, DeleteView
from django.views.generic \
         import ListView, DetailView
from django.urls import reverse_lazy

from apps.gallery.models import Gallery


class CreateGalleryView(CreateView):
    model = Gallery
    fields = ["title", "image"]
    success_url = reverse_lazy("list_gallery")
    template_name = "gallery/upload_gallery.html"

class ListGalleryView(ListView):
    model = Gallery
    fields = ["title", "image"]
    context_object_name = "galleries"
    template_name = "base.html"

class DetailGalleryView(DetailView):
    model = Gallery
    fields = "__all__"
    context_object_name = "gallery"
    template_name = "gallery/detail_gallery.html"

class UpdateGalleryView(UpdateView):
    model = Gallery
    fields = ["title", "image"]
    template_name = "gallery/update_gallery.html"
