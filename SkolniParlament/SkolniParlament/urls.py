from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from hlasovani import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vysledky/', views.vysledky),
    url(r'^hlasovani/', include('hlasovani.urls')),
    url(r'^kandidovat/', include('hlasovani.urlsKandidovat')),



]
