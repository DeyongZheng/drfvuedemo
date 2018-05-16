from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', view=TemplateView.as_view(template_name='frontend/home.html')),
    url(r'^api/', include('backend.urls')),
    url(r'^admin/', admin.site.urls),
]
