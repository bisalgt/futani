from django.urls import path

from apps.home.views import gallery

urlpatterns = [

    path("form/", gallery, name="gallery"),

]




