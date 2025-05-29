from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Task, TaskActivityLog
from .serializers import TaskSerializer
from django.shortcuts import render
from .utils import send_notification

class TaskAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            task = get_object_or_404(Task, pk=pk)
            serializer = TaskSerializer(task)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            send_notification(f"Task '{task.title}' created by {request.user.username}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        old_status = task.status
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            new_task = serializer.save()
            # Log status change
            if old_status != new_task.status:
                TaskActivityLog.objects.create(
                    task=new_task,
                    changed_by=request.user,
                    change=f"Status changed from {old_status} to {new_task.status}",
                )
                # WebSocket notification
                send_notification(f"Task '{task.title}' updated by {request.user.username}")
            return Response(TaskSerializer(new_task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response({"message": "Task deleted."}, status=status.HTTP_204_NO_CONTENT)


def notification_view(request):
    return render(request, "notifications.html")
