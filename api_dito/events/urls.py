from django.conf.urls import url
from django.conf.urls import url,include
from . import views
from api_dito.events.api import EventResource
urlpatterns = [
    # ex: /polls/

    url(r'^$', views.index, name='index'),
    url(r'events/', include(EventResource.urls())),

]