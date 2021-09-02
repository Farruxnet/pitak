from . serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from drf_yasg.utils import swagger_auto_schema

class ProvinceApiView(APIView):
    def get(self, request):
        """
        Viloyatlar ro'yxati


        ---
        """
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
        """
        Tumanlar ro'yxati chiqadi id ga qiymat sifatida viloyat idsi beriladi,

        natijada shu viloyatga tegishli barcha tumanlar chiqariladi.

        ---
        """
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
        """
        Barcha tumanlar ro'yxati


        ---
        """
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
        """
        Avtomobillar ro'yxati


        ---
        """
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
        """
        Yo'nalishlar ro'yxati qaytadi

        Misol => Navoiy-Toshkent-Navoiy yo'nalishi
        :id - yo'nalish idis
        :a_deriction - viloyat idsi
        :b_deriction  - viloyat idsi
        :c_deriction - viloyat idis
        """
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
