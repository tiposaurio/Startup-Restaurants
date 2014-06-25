from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('apps.auth.views',
	url(r'^register_user$', 'register_user', name='register_user'), # registro de usuario
	url(r'^register_success$', 'register_success', name='register_success'), # registro correcto
	url(r'^register_confirm/(?P<activation_key>\w+)/', 'register_confirm', name='register_confirm'), # confirmacion de cuenta
	url(r'^login$', login, {'template_name': 'auth/login_user.html', }, name="login"), # login
	url(r'^home$', 'home', name='home'), # home de usuario
	
	
	
		
)