from django.urls import path, include
from . import views
from . import routers

app_name = 'Users'


urlpatterns = [
   
    path('', include(routers.users_router.urls)),

]