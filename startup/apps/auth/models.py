# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural=u'User profiles'

class MenuUser(models.Model):
	nombre = models.CharField(max_length=200)
	icono = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	estado = models.BooleanField(default=1)
	def __unicode__(self):
	    return self.nombre

class TipoNuip(models.Model):
    nombretiponuip = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombretiponuip  

class PersonaUser(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    tiponuip = models.ForeignKey(TipoNuip)
    nuip = models.CharField(max_length=200, help_text='Número Único de Identificación Personal')
    telefono = models.CharField(max_length=200)

    imagen_persona = models.ImageField(upload_to='personas/%Y%m%d', verbose_name='Imagén')

    registered_at = models.DateTimeField(auto_now_add=True)
    modified_in = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User)

    def __unicode__(self):
        return self.nombres


