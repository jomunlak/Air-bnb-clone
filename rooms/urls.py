from django.urls import path
from rooms import views as room_views

app_name = "rooms"


urlpatterns = [
    path("<int:pk>", room_views.RoomDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", room_views.EditRoomView.as_view(), name="edit"),
    path("<int:pk>/photos/", room_views.Photos.as_view(), name="photos"),
]
