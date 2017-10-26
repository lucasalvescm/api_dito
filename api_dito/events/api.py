from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from api_dito.events.models import Event


class EventResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'title',
        'description': 'description',
    })

    def list(self):
        return Event.objects.all()