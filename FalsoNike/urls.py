from django.contrib import admin
from django.urls import path, include

from FalsoNike.views import  index,login_view, logout_view,RegistrarUsuario
from django.conf import settings
from django.conf.urls.static import static
#from users.views import Login


urlpatterns = [
    path('', index, name = 'index'),

    path('admin/', admin.site.urls),

    path('Nike/', include('Nike.urls')),
    path('usuarios/',include('users.urls')),

    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('RegistrarUsuario/',RegistrarUsuario.as_view(), name = 'RegistrarUsuario'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)