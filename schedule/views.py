from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Schedule
from .serializers import ScheduleSerializer


def index(request):
    return HttpResponse("")


class ScheduleList(APIView):
    def get(self, request):
        all_schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(all_schedule, many=True)
        return Response(serializer.data)

    def post(self):
        pass
