from django.urls import path
from apps.gallery.views \
        import CreateGalleryView, ListGalleryView, UpdateGalleryView, DetailGalleryView, GalleryView


urlpatterns = [
    path("upload_gallery/", CreateGalleryView.as_view(), name="upload_gallery"),
    path("list_gallery/", ListGalleryView.as_view(), name="list_gallery"),
    path("", GalleryView.as_view(), name="gallery"),
]
