from django.contrib import admin
from django.urls import path
from recipe import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.recipes),  
    path('update_recipe/<id>', views.update_recipe, name='update_recipe'),  
    path('delete_recipe/<id>', views.delete_recipe, name='delete_recipe'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)