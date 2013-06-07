from django.views.generic.list import ListView
from django.utils import timezone

from .models import Tap

class TapListView(ListView):

    model = Tap

    def get_context_data(self, **kwargs):
        context = super(TapListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context