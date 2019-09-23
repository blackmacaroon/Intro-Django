from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')      #the model information we wish to export

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer    #the rows from the database we want to show as a result
    queryset = PersonalNote.objects.all()