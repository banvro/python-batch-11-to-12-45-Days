from rest_framework import serializers
from xyzapi.models import MyTodo


class TodoSerializer(serializers.ModelSerializer):
    class Meta():
        model = MyTodo
        fields = "__all__"