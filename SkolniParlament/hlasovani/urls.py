from django.conf.urls import url
from . import views

urlpatterns = [
    #/hlasovani/
    #url(r'^$', views.hlasovani, name='hlasovani')

    #/hlasovani/token
    url(r'^(?P<Student_token>)$', views.hlasovani, name='hlasovani'),

]
