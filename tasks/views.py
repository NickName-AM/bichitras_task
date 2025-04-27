from rest_framework import viewsets, permissions

from tasks.models import Task
from tasks.serializers import TaskSerializer
from tasks.permissions import IsTaskOwner

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method in ["GET", "PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated(), IsTaskOwner()]
        
        return [permissions.IsAuthenticated()]
