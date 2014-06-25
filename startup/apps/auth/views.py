# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import *
from models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone

from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth import authenticate, login



def register_success(request):
    return render_to_response('auth/register_success.html', {}, context_instance=RequestContext(request))

def register_user(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form
        if form.is_valid():
            form.save()  # guardar el usuario a la base de datos si el formulario es válido
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]            
            activation_key = hashlib.sha1(salt+email).hexdigest()            
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            
            #Get usuario por nombre de usuario
            user=User.objects.get(username=username)

                
            print "------> estado del usuario es :",user.is_active

            # Crear y guardar perfil de usuario                                                                                                                                  
            new_profile = UserProfile(user=user, activation_key=activation_key, 
                key_expires=key_expires)
            new_profile.save()

            # Enviar correo electrónico con la clave de activación
            email_subject = 'STARTUP - RESTAURANTS'
            email_body = "Hey %s, Gracias por registrarte. Para activar su cuenta, haga clic en este enlace dentro \
            48hours http://127.0.0.1:8000/register_confirm/%s" % (username, activation_key)

            send_mail(email_subject, email_body, 'edwin.calsin.academico@gmail.com',
                [email], fail_silently=False)

            return HttpResponseRedirect('register_success')
    else:
        args['form'] = RegistrationForm()

    return render_to_response('auth/register_user.html', args, context_instance=RequestContext(request))


def register_confirm(request, activation_key):
    #comprobar si el usuario ya está conectado y si él se redirige a otra dirección URL, por ejemplo, Home
    if request.user.is_authenticated():
        HttpResponseRedirect('index')

    #comprobar si hay UserProfile que coincide con la clave de activación (si no entonces mostrar 404)
    user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

    #comprobar si ha expirado la clave de activación, si hase luego hacer confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('auth/confirm_expired.html')

    #si la llave no ha expirado Guardar usuario y lo establece como activa y hacer alguna plantilla para confirmar la activación
    user = user_profile.user
    user.is_active = True
    user.is_staff = True
    user.save()
    return render_to_response('auth/confirm_user.html')

def login(request):
    return render_to_response('auth/login_user.html', {}, context_instance=RequestContext(request))


@login_required()
def home(request):
    messages.success(request, "Bienvenido !!!")
    menu = MenuUser.objects.all()

    #print "---- recuperando id del usuario -->",request.user.id

    #datospersona =PersonaUser.objects.get(id=request.user.id)

    #print " mis datos persona --->",datospersona.imagen_persona

    return render_to_response('auth/user/home.html', {'user': request.user,'menu':menu}, context_instance=RequestContext(request))
    #return render_to_response('auth/user/home.html', {'user': request.user,'menu':menu, 'datospersona':datospersona}, context_instance=RequestContext(request))
    #return render_to_response('auth/user/home.html', {'user': request.user}, context_instance=RequestContext(request))


