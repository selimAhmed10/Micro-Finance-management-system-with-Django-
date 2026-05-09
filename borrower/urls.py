from django.urls import path
from . import views

urlpatterns = [
     path('dashboard/', views.dashboard),
    path('members/<int:group_id>/', views.group_members),
    path('view/', views.borrower_list),
    path('add/<int:group_id>/', views.add_member),
    path('edit/<int:id>/', views.edit_member),
    path('delete/<int:id>/', views.delete_member),
]