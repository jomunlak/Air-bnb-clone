from django.views.generic import ListView, DetailView, UpdateView
from django.utils import timezone
from django.http import Http404
from . import models as room_models


# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = room_models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = "page"
    ordering = "pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class RoomDetail(DetailView):

    """Room Detail Definition"""

    model = room_models.Room


class EditRoomView(UpdateView):

    """Room Edit View Definition"""

    template_name = "rooms/room_edit.html"
    model = room_models.Room
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "max_guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )

    def get_object(self, queryset=None):
        room = super().get_object(queryset)
        # if room.host.pk != self.request.user.pk:
        #     raise Http404

        return room


class Photos(DetailView):
    model = room_models.Room
    template_name = "rooms/room_photos.html"
