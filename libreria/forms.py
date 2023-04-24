from django import forms
from .models import equipo, comentario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class equipoform(forms.ModelForm):
    class Meta:
        model = equipo
        fields = '__all__'

class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False, label="Foto de perfil")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields }    


class ComentarioForm(forms.ModelForm):
    
    texto = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí...'}))
    
    class Meta:
        model = comentario
        fields = ('texto',)
        
class EditarPerfilForm(UserChangeForm):
    password = None 
    avatar = forms.ImageField(required=False, label='Imagen de perfil')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'avatar')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }
        error_messages = {
            'username': {
                'unique': 'Este nombre de usuario ya está en uso.'
            },
            'email': {
                'unique': 'Este correo electrónico ya está en uso.'
            },
        }           