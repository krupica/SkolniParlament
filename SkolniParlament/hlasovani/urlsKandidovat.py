from django.conf.urls import url
from . import views

urlpatterns = [
    #/kandidovat/
    url(r'^$', views.kandidovattest, name='kandidovattest'),
    #/kandidovat/token/
    url(r'^(?P<Kandidat_token>[-\w]+)/$', views.kandidovat, name='kandidovat'),
]
