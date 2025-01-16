from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form_elements, name='form-elements'),
    path('form-layout/', views.form_layout, name='form-layout'),
    path('hello/', views.hello, name='hello'),
]