from django.shortcuts import render
from django.utils import timezone

from .models import Evenement

# Create your views here.
def index(request):
    future_events_list = Evenement.objects.filter(date__gte=timezone.now()).order_by('date')
    context = {'future_events': future_events_list}
    return render(request, 'umm/index.html', context)
