# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address','class':'form-control input-sm'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombres','class':'form-control input-sm'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Apellidos','class':'form-control input-sm'}))
    
    # ---
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese un usuario','class':'form-control input-sm'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'su contraseña','class':'form-control input-sm','type':'password'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'repita su contraseña','class':'form-control input-sm'}))


     

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2','is_active')

#limpiar el campo de correo electrónico
def clean_email(self):
    email = self.cleaned_data["email"]
    try:
        User._default_manager.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError('el email ya existe')

#modify save() método para que podamos establecer user.is_active en False cuando nos creamos nuestro usuario
def save(self, commit=True):        
    user = super(RegistrationForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    
    if commit:
        
        user = RegistrationForm.user  # instanciando mi objeto user
        
        print "------> ingresando objeto //-->",user


        user.is_active = False
        print "-->> entrando al metodo guardar usuario -->> estado user es: ",user.is_active
    
        user.save()

        print "se guardo el usuario"
    return userx

