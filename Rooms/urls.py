from django.urls import path, include
from . import views
from . import routers

app_name = 'Rooms'


urlpatterns = [
   
    path('', include(routers.room_router.urls)),
    path('list/', views.RoomListCreateAPI.as_view(), name = views.RoomListCreateAPI.name),
    path('get/<int:pk>', views.RoomRetrieveAPI.as_view(), name = views.RoomRetrieveAPI.name),
    path('update/<int:pk>', views.RoomUpdateAPI.as_view(), name = views.RoomUpdateAPI.name),
    path('delete/<int:pk>', views.RoomDeleteAPI.as_view(), name = views.RoomDeleteAPI.name),
  

]