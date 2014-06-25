from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    url(r'^', include('apps.web.urls')), # index principal de la web
    url(r'^', include('apps.auth.urls')), # autenticacion user
    
    url(r'^logout$', logout, {'template_name': 'web/index.html', }, name="logout"),
)
