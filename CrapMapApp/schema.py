from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import CrapMapApp

class NoteType(DjangoObjectType):

    class Meta:
        model = CrapMapApp
        interfaces = (graphene.relay.Node,) #tuple - if there's only one thing, leave the comma so it knows it's a tuple
    
class Query(graphene.ObjectType):
    notes = graphene.List(NoteType)

    def resolve_notes(self, info):
        return CrapMapApp.objects.all()

schema = graphene.Schema(query=Query)