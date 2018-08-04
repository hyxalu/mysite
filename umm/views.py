from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect, reverse
from django.utils import timezone

from .models import Evenement
from .forms import ContactForm

from . import urls

# Create your views here.
def index(request):
    future_events_list = Evenement.objects.filter(date__gte=timezone.now()).order_by('date')
    context = {'future_events': future_events_list}
    return render(request, 'umm/index.html', context)

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, "umm/email.html", {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            given_name = form.cleaned_data['given_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            msg = "{0} {1} ({2}) nous envoie le message suivant\r\n{3}".format(given_name , name, from_email, message)
            try:
                send_mail(subject, msg, from_email, ['schaillie@gmail.com'])
            except:
                return HttpResponse('Error while sending mail.')
            return redirect('umm:success')
        else:
            return HttpResponse('Form invalid.')


def successView(request):
    return render(request, 'umm/success.html')
