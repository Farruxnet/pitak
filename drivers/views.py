from . serializer import DriverSerializer, DriverCartSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Driver, DriverCart

class DriverApiView(APIView):
    def post(self, request):
        try:
            serializer = DriverSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 201,
                    'data': serializer.data
                })
            return Response({
                'status': 201,
                'data': serializer.data
            })
        except Exception as e:
            raise
