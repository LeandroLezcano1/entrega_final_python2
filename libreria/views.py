from .models import equipo, comentario
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import equipoform, UserRegisterForm, ComentarioForm, EditarPerfilForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfil
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def about_me(request):
    return render(request, 'paginas/about_me.html')

def equipos(request):
    equipos = equipo.objects.all()
    return render(request, 'equipos/index.html', {'equipos': equipos})

@login_required
def crear(request):
    formulario = equipoform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('equipos')
    return render(request, 'equipos/crear.html', {'formulario': formulario})

@login_required
def editar(request, id):
    eq = equipo.objects.get(id=id)
    formulario = equipoform(request.POST or None, request.FILES or None, instance=eq)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('equipos')
    return render(request, 'equipos/editar.html', {'formulario': formulario})

@login_required
def eliminar(request, id):
    eq = equipo.objects.get(id=id)
    eq.delete()
    return redirect('equipos')

def signup(request):
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            messages.success(request, f'Usuario {username} creado')
            return redirect('inicio')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'paginas/signup.html', context)

def detalle_equipo(request, equipo_id):
    obj_equipo = get_object_or_404(equipo, id=equipo_id)
    comentarios = comentario.objects.filter(equipo=obj_equipo)
    context = {
        'equipo': obj_equipo,
        'comentarios': comentarios
    }
    return render(request, 'detalle_equipo.html', context)

@login_required
def crear_comentario(request, equipo_id):
    equipo_obj = get_object_or_404(equipo, pk=equipo_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.equipo = equipo_obj
            comentario.save()
            return redirect('detalle_equipo', equipo_id=equipo_id)
    else:
        form = ComentarioForm()
    return render(request, 'paginas/crear_comentario.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            usuario = form.save(commit=False)
            if 'avatar' in request.FILES:
                usuario.avatar = request.FILES['avatar']
            usuario.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})


