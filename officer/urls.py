from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('view/',views.view_officer),
    path('create/',views.create_officer),
    path('edit/<int:id>/',views.modify_officer),
    path('delete/<int:id>/',views.delete_officer),
    
]