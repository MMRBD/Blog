from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='p_home'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('edit/<contact_id>', views.edit, name='edit'),
    path('delete/<contact_id>', views.delete, name='delete'),
]
