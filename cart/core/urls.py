from django.contrib import admin
from django.urls import path
from recipe import views  
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipes), 
    # path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('update_recipe/<id>', views.update_recipe, name='update_recipe'),  
    path('delete_recipe/<id>', views.delete_recipe, name='delete_recipe'),  
    path('accounts/', include('django.contrib.auth.urls')),  
    path('accounts/register/', views.register, name='register'), 

]

# Add media URL configuration
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)