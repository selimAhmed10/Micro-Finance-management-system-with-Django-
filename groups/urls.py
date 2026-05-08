from django.urls import path
from . import views
urlpatterns = [
    path('',views.view_group),
    path('create/',views.create_group),
    path('edit/<int:id>/',views.modify_group),
    path('delete/<int:id>/',views.delete_group),
]
