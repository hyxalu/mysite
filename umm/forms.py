from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', required=True)
    given_name = forms.CharField(label='Prénom', required=True)
    from_email = forms.EmailField(label='Votre adresse email', required=True)
    subject = forms.CharField(label='Sujet de votre message', required=True)
    message = forms.CharField(label='Votre message', widget=forms.Textarea, required=True)


class BroadcastForm(forms.Form):
    subject = forms.CharField(label='Sujet de votre message', required=True)
    message = forms.CharField(label='Votre message', widget=forms.Textarea, required=True)