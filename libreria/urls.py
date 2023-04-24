from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='paginas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='paginas/logout.html'), name='logout'),
    path('', views.inicio, name='inicio'),
    path('about_me/', views.about_me, name='about_me'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipos/crear/', views.crear, name='crear'),
    path('equipos/editar/<int:id>/', views.editar, name='editar'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('signup/', views.signup, name='signup'),
    path('equipos/<int:equipo_id>/', views.detalle_equipo, name='detalle_equipo'),
    path('equipos/<int:equipo_id>/comentar/', views.crear_comentario, name='crear_comentario'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)