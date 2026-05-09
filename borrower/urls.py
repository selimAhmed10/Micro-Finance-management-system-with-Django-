from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('view/', views.view_borrower),
    path('create/', views.borrower_create),
    path('edit/<int:id>/', views.borrower_edit),
    path('delete/<int:id>', views.borrower_delete),
]