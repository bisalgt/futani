from django.views.generic.edit \
        import CreateView, UpdateView, DeleteView
from django.views.generic \
         import ListView, DetailView, TemplateView
from django.urls import reverse_lazy


from apps.gallery.models import Gallery


class CreateGalleryView(CreateView):
    model = Gallery
    fields = ["title", "image"]
    success_url = reverse_lazy("home")
    template_name = "gallery/upload_gallery.html"

class ListGalleryView(ListView):
    print("list of gallery items")
    model = Gallery
    fields = ["title", "image"]
    # context_object_name = "galleries"
    template_name = "partials/gallery.html"

    def get_context_data(self, **kwargs):
        print("inside context")
        context = super().get_context_data(**kwargs)
        context["galleries"] = Gallery.objects.all() 
        context["message"] = "This is a message from context data" 
        return context
    
class GalleryView(TemplateView):
    template_name = "base.html"
    print("template view")
    
    def get_context_data(self, **kwargs):
        print("inside context")
        context = super().get_context_data(**kwargs)
        context["galleries"] = Gallery.objects.all() 
        context["message"] = "This is a message from context data" 
        return context


class DetailGalleryView(DetailView):
    model = Gallery
    fields = "__all__"
    context_object_name = "gallery"
    template_name = "gallery/detail_gallery.html"

class UpdateGalleryView(UpdateView):
    model = Gallery
    fields = ["title", "image"]
    template_name = "gallery/update_gallery.html"
