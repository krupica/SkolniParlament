from django.conf.urls import url
from . import views

urlpatterns = [
    #/hlasovani/
    url(r'^$', views.hlasovanitest, name='hlasovanitest'),
    #/hlasovani/token/
    url(r'^(?P<Student_token>[-\w]+)/$', views.hlasovani, name='hlasovani'),
]
