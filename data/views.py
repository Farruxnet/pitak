from . serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from drf_yasg.utils import swagger_auto_schema

class ProvinceApiView(APIView):
    def get(self, request):
        try:
            province = Province.objects.all()
            serializer = ProvinceSerializer(province, many=True)
            return Response({
                'status': 200,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error': "error"+str(e)
            })

class DistrictApiView(APIView):
    def get(self, request, pk):
        try:
            serializer = DistrictSerializer(District.objects.filter(province=pk), many=True)
            return Response({
                'status': 200,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error': "error"+str(e)
            })

class DistrictApiAllView(APIView):
    def get(self, request):
        try:
            serializer = DistrictSerializer(District.objects.all(), many=True)
            return Response({
                'status': 200,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error': "error"+str(e)
            })

class AutomobileApiView(APIView):
    def get(self, request):
        try:
            serializer = AutomobileSerializer(Automobile.objects.all(), many=True)
            return Response({
                'status': 200,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error': "error"+str(e)
            })

class DerictionApiView(APIView):
    def get(self, request):
        try:
            serializer = DerictionSerializer(Deriction.objects.all(), many=True)
            return Response({
                'status': 200,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error': "error"+str(e)
            })
