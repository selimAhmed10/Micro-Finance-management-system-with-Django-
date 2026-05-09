from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('list/', views.borrower_list),
    path('add/<int:group_id>/', views.add_member),
    path('edit/<int:id>/', views.edit_member),
    path('delete/<int:id>/', views.delete_member),
]