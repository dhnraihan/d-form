from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path("curd", views.curd, name="curd"),
    path('form1', views.form_elements, name='form-elements'),
    path('form-layout/', views.form_layout, name='form-layout'),
    path('hello/', views.hello, name='hello'),
#    CURD
    path('form', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('<int:pk>/update/', views.item_update, name='item_update'),
    path('<int:pk>/delete/', views.item_delete, name='item_delete'),
]