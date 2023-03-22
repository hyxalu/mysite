from django import forms
from .models import Profile
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    given_name = forms.CharField(label='Prénom', required=True)
    name = forms.CharField(label='Nom', required=True)
    from_email = forms.EmailField(label='Votre adresse email', required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(), error_messages={'required': 'Vous devez réussir le test reCaptcha.'})
    subject = forms.CharField(label='Sujet de votre message', required=True)
    message = forms.CharField(label='Votre message', widget=forms.Textarea, required=True)


class BroadcastForm(forms.Form):
    recipients = forms.ModelMultipleChoiceField(
        label='Destinataires',
        required=True,
        queryset=Profile.objects.filter(user__groups__name='Newsletter').order_by('user__last_name'),
        widget=forms.CheckboxSelectMultiple
    )
    subject = forms.CharField(label='Sujet de votre message', required=True)
    message = forms.CharField(label='Votre message', widget=forms.Textarea, required=True)