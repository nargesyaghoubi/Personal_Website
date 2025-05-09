
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('Narges/', admin.site.urls),
    path('', include('main.urls')),
    path('contact/', include('contact.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)