from django.urls import path, re_path
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    # path('', views.api_root),
    path('schema/', schema_view, name='shema'),
]

urlpatterns = format_suffix_patterns(urlpatterns)