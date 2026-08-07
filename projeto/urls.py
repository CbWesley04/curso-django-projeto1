from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), #/
   # path('recipes/', include('recipes.urls')), # domínio.com/recipes/
]

    # SOLICITATION -> HTTP REQUEST -> CLIENTE PEDE
    # RETURN -> HTTP RESPONSE -> SERVIDOR RESPONDE