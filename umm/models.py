from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Place(models.Model):
    """
    Model representing a location
    """
    title = models.CharField(max_length=512, help_text="Entrez le nom de l'endroit")

    country = models.CharField(max_length=512, help_text="Entrez le nom du pays", blank=True)

    town = models.CharField(max_length=512, help_text="Entrez le nom de la ville")

    postCode = models.PositiveSmallIntegerField("Entrez le code postal", blank=True)

    address = models.CharField(max_length=512, help_text="Entrez l'adresse", blank=True)

    note = models.CharField(max_length=4096, help_text="Entrez une note (une explication)", blank=True)

    def __str__(self):
        """
        String for representing the Place Model object
        """
        return self.title


class Evenement(models.Model):
    """
    Model representing an event : concert, parade, ...
    """
    title = models.CharField(max_length=512, help_text="Entrez le titre de l'événement")

    date = models.DateField(help_text="Date de l'événement")

    time_begin = models.TimeField(help_text="Heure de l'événement", blank=True, null=True)

    place = models.ForeignKey(
        Place,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    time_arrival = models.TimeField(help_text="Heure d'arrivée des musiciens", blank=True, null=True)
    CLASSIC = 'CL'
    CASUAL = 'CA'
    BLACK = 'BL'
    OUTFIT_CHOICES = (
        (CLASSIC, 'Classique (Haut blanc, bas noir)'),
        (CASUAL, 'Décontracté'),
        (BLACK, 'Noir intégral (Haut noir, bas noir)'),
    )
    outfit = models.CharField(
        max_length=2,
        blank = True,
        choices=OUTFIT_CHOICES,
        default=CLASSIC,
    )

    def __str__(self):
        """
        String for representing the Evenement Model object
        """
        return str.format("{} ({} - {})", self.title, self.place.title, self.date)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("send_email", "Can send an email"),
        )

    def __str__(self):
        """
        String for representing the Profile Model object
        """
        return str.format("{} {}", self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
