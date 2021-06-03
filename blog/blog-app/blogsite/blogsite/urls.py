from django.contrib import admin
from django.urls import path
from blogweb.views import *
from django.urls import include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('blog/', include('blogweb.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
