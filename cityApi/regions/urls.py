from django.urls import path, re_path
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
	
urlpatterns = [
	#STATES
    path('states/', views.StateList.as_view(), name='state-list'),
    path('states/<int:pk>/', views.StateDetail.as_view(), name='state-detail'),

    #CITIES
    path('cities/', views.CityList.as_view(), name='city-list'),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name='city-detail')
]		

urlpatterns = format_suffix_patterns(urlpatterns)