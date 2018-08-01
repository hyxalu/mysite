from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Evenement
from .forms import ContactForm

# Create your views here.
def index(request):
    future_events_list = Evenement.objects.filter(date__gte=timezone.now()).order_by('date')
    context = {'future_events': future_events_list}
    return render(request, 'umm/index.html', context)

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['schaillie@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "umm/email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
