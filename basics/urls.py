from django.conf.urls import url, include

from . import views

app_name = 'basics'
urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^accounts/', include('registration.backends.hmac.urls', namespace='registration')),
    url(r'^$', views.index, name='index'),
]
