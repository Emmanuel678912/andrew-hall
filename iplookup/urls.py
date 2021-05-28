from django.urls import path
from . import views


urlpatterns = [
    path('', views.input_page, name='input_page'),
    path('generate', views.generate_page, name='generate_page'),
    path('view', views.view_tables, name='view_tables')
    
]
