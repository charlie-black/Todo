from rest_framework import serializers, viewsets
from.models import Todo
from.serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()#this tells us to use the all the objects
    serializer_class = TodoSerializer
