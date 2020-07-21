from rest_framework.routers import DefaultRouter
from . import views

#The various routers

customers_router = DefaultRouter()

customers_router.register(r'customers', views.CustomerViewset)