from rest_framework.routers import DefaultRouter
from . import views

#The various routers

users_router = DefaultRouter()

users_router.register(r'users', views.UserViewset)