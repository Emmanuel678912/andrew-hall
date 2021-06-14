from django.urls import path
from . import views


urlpatterns = [
    path('', views.input_page, name='input_page'),
    path('generate', views.generate_page, name='generate_page'),
    path('view', views.view_tables, name='view_tables'),

    # pages for deleting rows
    path('delete_row_a/<str:pk>/', views.deleteRowA, name='delete_row_a'),
    path('delete_row_b/<str:pk>/', views.deleteRowB, name='delete_row_b'),
    path('delete_row_c/<str:pk>/', views.deleteRowC, name='delete_row_c'),
    path('delete_row_d/<str:pk>/', views.deleteRowD, name='delete_row_d'),
    path('delete_row_e/<str:pk>/', views.deleteRowE, name='delete_row_e'),
    path('delete_row_f/<str:pk>/', views.deleteRowF, name='delete_row_f'),
    path('delete_row_g/<str:pk>/', views.deleteRowG, name='delete_row_g'),
    path('delete_row_h/<str:pk>/', views.deleteRowH, name='delete_row_h'),
    
]
