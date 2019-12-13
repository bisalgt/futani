from django.urls import path

from apps.home.views import gallery, feedback, GalleryListView

urlpatterns = [

    path("gallery/", GalleryListView.as_view(), name="gallery_list"),
    path("gallery_form/", gallery, name="gallery_form"),
    path("feedback_form/", feedback,  name="feedback_form"),

]




