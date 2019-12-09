from django.urls import path

from apps.home.views import gallery, feedback

urlpatterns = [

    path("form/", gallery, name="gallery"),
    path("feedback_form/", feedback,  name="feedback_form"),

]




