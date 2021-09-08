from . serializer import DriverSerializer, DriverCartSerializer, DriverGetSerializer, DriverCartGetSerializer, DriverCartPutSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Driver, DriverCart
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from users.models import User
from drivers.models import Driver, DriverCart
from rest_framework.renderers import JSONRenderer

# Haydovchi elon qo'shish
class DriverApiView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    @swagger_auto_schema(request_body = DriverSerializer)
    def post(self, request):
        """
        Haydovchi e'lon qo'shish

        POST http://127.0.0.1:8000/api/v1/driver/create/
        :user
        :deriction
        :district
        :automobile
        :phone_number_one
        :phone_number_two
        :cooling_system
        :baggage
        :fuel
        :sex
        :create_at
        :status
        """
        try:
            serializer = DriverSerializer(data = request.data)
            if serializer.is_valid():
                user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
                user = User.objects.get(id=user_id)
                if Driver.objects.filter(user=user).exists():
                    return Response({
                        'status': 400,
                        'error': "Ushbu foydalanuvchida e'lon mavjud"
                    })
                serializer.save(user=user)
                return Response({
                    'status': 201,
                    'data': serializer.data
                })

        except Exception as e:
            return Response({
                'status': 400,
                'data': str(e)
            })

# Haydovchi elonini ko'rish
class DriverGetApiView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def get(self, request):
        """
        Haydovchi e'lonini to'liq ko'rish


        Response
        :id
        :user
        :deriction
        :district
        :automobile
        :phone_number_one
        :phone_number_two
        :cooling_system
        :baggage
        :fuel
        :sex
        :create_at
        :status
        """
        try:
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            driver = Driver.objects.get(user__id=user_id, status=True)
            serializer = DriverGetSerializer(driver)
            if driver:
                return Response({
                    'status': 200,
                    'data': serializer.data
                })

        except Exception as e:
            return Response({
                'status': 400,
                'data': str(e)
            })

# Haydovchi qidiruv eloni qo'shish o'zgartirish, ko'rish
class DriverCartPutApiView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    @swagger_auto_schema(request_body = DriverCartPutSerializer)
    def put(self, request):
        """
        Haydovchi qidiruvga bergan eloni tahrirlash.

        ---
        """
        try:
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            driver = DriverCart.objects.get(driver__user=user, status=True)
            serializer = DriverCartPutSerializer(driver, data = request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({
                'status': 200,
                'data': serializer.data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'error': "Avtorizatsiydan o'tmadi."+str(e)
            })

class DriverCartPostApiView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body = DriverCartSerializer)
    def post(self, request, format=None):
        """
        Haydovchi Qidiruvga e'lon berish


        berilgan elon bilan haydovchilar qidiruvda filterlanadi
        POST
        :empty_count
        :current_location
        :finish_location
        :delivery
        """
        try:
            serializer = DriverCartSerializer(data = request.data)
            if serializer.is_valid():
                user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
                user = User.objects.get(id=user_id)
                driver = Driver.objects.get(user__id=user_id, status=True)
                if DriverCart.objects.filter(driver=driver, status=True).exists():
                    DriverCart.objects.filter(driver=driver, status=True).update(status=False)
                serializer.save(driver=driver)
                return Response({
                    'status': 201,
                    'data': serializer.data
                })
            return Response({
                'status': 201,
                'data': serializer.errors
            })

        except Exception as e:
            return Response({
                'status': 201,
                'data': str(e)
            })
class DriverCartGetApiView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        """
        Haydovchi qidiruvga berilgan e'lon ma'lumotlarini to'liq olish.


        Response
        :id
        :user
        :driver
        :delivery_user
        :empty_count
        :current_location
        :finish_location
        :delivery
        """
        try:
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            driver = DriverCart.objects.get(driver__user=user_id, status=True)
            serializer = DriverCartGetSerializer(driver)
            return Response({
                'status': 200,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error': str(e)
            })
