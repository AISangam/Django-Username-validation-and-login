from django.urls import path
from . import views
from .views import form_validation, get_data_from_db

urlpatterns=[
			path('', views.form_validation, name='form_validation'),
			path('get_data', views.get_data_from_db, name='get_data_from_db')
			]
