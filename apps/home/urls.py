from django.urls import path

from apps.home.views import gallery, feedback, GalleryListView, gallery_delete, feedback_delete, gallery_update, feedback_update

urlpatterns = [

    path("gallery/", GalleryListView.as_view(), name="gallery_list"),
    path("gallery/<int:id>/<str:slug>/delete/", gallery_delete, name="gallery_delete"),
    path("gallery/<int:id>/<str:slug>/", gallery_update, name="gallery_update"),
    path("feedback/<int:id>/<str:slug>/delete/", feedback_delete, name="feedback_delete"),
    path("feedback/<int:id>/<str:slug>", feedback_update, name="feedback_update"),
    path("gallery_form/", gallery, name="gallery_form"),
    path("feedback_form/", feedback,  name="feedback_form"),

]




