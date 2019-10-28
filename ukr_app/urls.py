from django.urls import path, include

from ukr_app import views

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('view/<int:pk>', views.link_view, name='link_view'),
    path('new', views.link_create, name='link_new'),
    path('edit/<int:pk>', views.link_update, name='link_edit'),
    path('delete/<int:pk>', views.link_delete, name='link_delete'),
]
