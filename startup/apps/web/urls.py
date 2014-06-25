from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.web.views',
	url(r'^$', 'index', name="index"), # cargando por defaul la pagina principal de la web

)