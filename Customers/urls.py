from django.urls import path, include
from . import views
from . import routers

app_name = 'Customers'


urlpatterns = [
   
    path('', include(routers.customers_router.urls)),

]