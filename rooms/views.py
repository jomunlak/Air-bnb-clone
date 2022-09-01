from django.views.generic import ListView
from django.utils import timezone
from . import models as room_models

# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = room_models.Room
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = "page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
