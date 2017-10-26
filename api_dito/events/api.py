from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from api_dito.events.models import Event
from django.shortcuts import get_object_or_404

class EventResource(DjangoResource):

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'title',
        'description': 'description',
    })

    def list(self):
    	return Event.objects.all()

    def detail(self,name):
    	print('name')
    	events = Event.objects.filter(title__contains=name)
    	return events