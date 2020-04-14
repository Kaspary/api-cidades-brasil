from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from . import views

app_name='users'


router = DefaultRouter()
router.register(r'', views.User, basename='user')

urlpatterns = [

	#USERS
    # path('', views.UserList.as_view(), name='user-list'),
    # path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('get-auth-token/', views.ObtainAuthTokenView.as_view(), name='get-auth-token'),
    path('get-new-auth-token/', views.NewAuthTokenView.as_view(), name='get-new-auth-token')
] + router.urls