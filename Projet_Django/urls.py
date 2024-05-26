from django.contrib import admin, auth
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Jeu',include('jeu.urls'),name='Jeu'),
    path('game/', include('game.urls', namespace='game')),
    path('',include('Student_Help.urls'),name='Student_Help'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),


    
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


