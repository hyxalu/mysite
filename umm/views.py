from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.html import strip_tags

from .models import Evenement, Profile
from .forms import ContactForm, BroadcastForm

import re

# Create your views here.


def index(request):
    future_events_list = Evenement.objects.filter(
        date__gte=timezone.now()).order_by('date')
    context = {'future_events': future_events_list}
    return render(request, 'umm/index.html', context)


def who(request):
    return render(request, 'umm/who.html')


def agenda(request):
    future_events_list = Evenement.objects.filter(
        date__gte=timezone.now()).order_by('date')
    context = {'future_events': future_events_list}
    return render(request, 'umm/agenda.html', context)


def archives(request):
    past_events_list = Evenement.objects.filter(
        date__lt=timezone.now()).order_by('-date')
    context = {'past_events': past_events_list}
    return render(request, 'umm/archives.html', context)


def detail_event(request, event_id):
    event = get_object_or_404(Evenement, pk=event_id)
    return render(request, 'umm/detail_event.html', {'event': event})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, "umm/contact.html", {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            given_name = form.cleaned_data['given_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            msg = "{0} {1} ({2}) nous envoie le message suivant\r\n{3}".format(
                given_name, name, from_email, message)
            try:
                email = EmailMessage(
                    subject,
                    msg,
                    'ne-pas-repondre@harmonie-maurage.be',
                    ["schaillie@gmail.com"])
                email.content_subtype = "html"
                email.send(True)
            except:
                return HttpResponse('Une erreur s\'est produite lors de l\'envoi de l\'email.')
            return redirect('umm:contact_success')
        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    form.non_field_errors("You must pass the reCAPTCHA test")
                    continue
            return render(request, "umm/contact.html", {'form': form})


@permission_required('umm.send_email', login_url='umm:login')
def email_members(request):
    if request.method == 'GET':
        form = BroadcastForm(
            initial={'recipients': Profile.objects.filter(user__groups__name='Newsletter')})
        return render(request, "umm/email_members.html", {'form': form})
    else:
        form = BroadcastForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # plain_message = strip_tags(message) # to be handled later
            recipients = form.cleaned_data['recipients']
            print(recipients)
            users = recipients.values_list('user__email', flat=True).distinct()
            try:
                p = re.compile('[^@]+@(skynet\.be|belgacom\.net)')
                users_skynet = [u for u in users if p.match(u)]
                users_other = [u for u in users if not p.match(u)]
                email = EmailMessage(
                    subject,
                    message,
                    'ne-pas-repondre@harmonie-maurage.be',
                    [],
                    users_other,
                    reply_to=["fabienne.dussenwart@gmail.com"])
                email.content_subtype = "html"
                email.send(True)
                for singleEmail in users_skynet:
                    email2 = EmailMessage(
                        subject,
                        message,
                        'ne-pas-repondre@harmonie-maurage.be',
                        [singleEmail],
                        [])
                    email2.send(True)
            except Exception as e:
                return HttpResponse('Une erreur s\'est produite lors de l\'envoi de l\'email.')
            return redirect('umm:email_members_success')
        else:
            return HttpResponse('Form invalid.')


@permission_required('umm.send_email', login_url='umm:login')
def email_members_success(request):
    return render(request, 'umm/email_members_success.html')


def contact_success(request):
    return render(request, 'umm/contact_success.html')
