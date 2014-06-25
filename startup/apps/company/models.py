# coding: utf-8
from django.db import models
from apps.auth.models import TipoNuip

# Create your models here.

class TipoRestaurante(models.Model):
	nombre = models.CharField(max_length=200)
	def __unicode__(self):
		return self.nombre


class Restaurante(models.Model):
	nombres = models.CharField(max_length=200, help_text='Nombre del restaurante')
	razonsocial = models.CharField(max_length=200, help_text='Razon Social')
	nit = models.CharField(max_length=200, help_text='Número de Identificación Tributaria')
	representante = models.CharField(max_length=200, help_text='Dueño del Restaurante')
	tiponuip = models.ForeignKey(TipoNuip)
	nuip = models.CharField(max_length=200, help_text='Número Único de Identificación Personal')
	paginaweb = models.CharField(max_length=200, help_text='www.miempresa.com')
	logo = models.ImageField(upload_to='restaurante/%Y%m%d', verbose_name='Imagén')
	registered_at = models.DateTimeField(auto_now_add=True)
	modified_in = models.DateTimeField(auto_now=True)

	def __unicode__(self):
	    return self.nombres



class Sucursal(models.Model):
	nombresucursal = models.CharField(max_length=200, help_text='Nombre de Sucursal')
	restaurante = models.ForeignKey(Restaurante)
	tiporestaurante = models.ForeignKey(TipoRestaurante)
	direccion = models.CharField(max_length=200, help_text='direccion, departamento, pais')	
	telefono = models.IntegerField()
	fax = models.IntegerField()
	celular = models.IntegerField()
	latitud = models.CharField(max_length=200)
	longitud = models.CharField(max_length=200)
	distancia = models.CharField(max_length=200)
	registered_at = models.DateTimeField(auto_now_add=True)
	modified_in = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nombresucursal

class TipoComida(models.Model):
	nombrecomida = models.CharField(max_length=200, help_text='Tipo de comida ')

	def __unicode__(self):
		return self.nombrecomida


class ServicioComida(models.Model):
	platocomida = models.CharField(max_length=200, help_text='Nombre del plato / comida')
	precio = models.IntegerField()
	tipocomida = models.ForeignKey(TipoComida)
	sucursal = models.ForeignKey(Sucursal)
	registered_at = models.DateTimeField(auto_now_add=True)
	modified_in = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.platocomida
