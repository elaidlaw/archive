from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input', views.new_image_to_annotate, name='input'),
    path('input/<str:img>', views.input, name='input-img'),
    path('list', views.images_list, name='img-list'),
]
