from rest_framework import serializers
from apptask.models import Project, Task, UserProfile


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'id', 'title', 'description', 'person')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'id', 'title', 'description', 'due_date', 'project', 'person')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'id', 'username', 'email', 'password', 'role')