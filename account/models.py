from django.db import models
from django.conf import settings
import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from . import signals

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	STATUS_CHOICES = (
		('Donor', 'Donor'),
		('Receiver', 'Receiver'),		
	)
	BLOOD_CHOICES = (
		('A+', 'A+'),
		('B+', 'B+'),
		('O+', 'O+'),
		('A-', 'A-'),
		('B-', 'B-'),
		('O-', 'O-'),
		('AB-', 'AB-'),
		('AB+', 'AB+'),
	)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='receiver')
	blood_group = models.CharField(max_length=3, choices=BLOOD_CHOICES, default='a+')
	hospital = models.CharField(max_length=50, default='none')
	address = models.TextField(default='none')

	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)
