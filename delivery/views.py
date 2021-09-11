from . serializer import DeliveryGetSerializer, DeliveryPutSerializer, DeliveryPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Delivery
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from users.models import User
from rest_framework.renderers import JSONRenderer
from drivers.models import DriverCart
from customer.serializer import DriverCartGetAllSerializer
from data.models import Province, District


# Pochtani view qismi qo'shish
class DeliveryPostView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(request_body = DeliveryPostSerializer)
    def post(self, request):
        """
        Mijoz pochta yuborish


        -----------
        """
        try:
            from rest_framework.pagination import PageNumberPagination
            paginator = PageNumberPagination()

            serializer = DeliveryPostSerializer(data = request.data)
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)

            driver_list = DriverCart.objects.filter(
                current_location=Province.objects.get(id=request.data['delivery_current_location']),
                finish_location=Province.objects.get(id=request.data['delivery_finish_location']),
                driver__district__in=[request.data['delivery_finish_district']],
                delivery=True,
                status=True
            )
            page = paginator.paginate_queryset(driver_list, request)

            # Agar yulovchida faol elon bo'lsa va yana e'lon qo'shmoqchi bo'lsa
            # oldingi faol eloni nofaolga o'zgartiradi
            if Delivery.objects.filter(user=user, status=True).exists():
                Delivery.objects.filter(user=user, status=True).update(status=False)

            serializer_result = DriverCartGetAllSerializer(page, many=True)

            if serializer.is_valid():
                serializer.save(user=user)
                return paginator.get_paginated_response({
                    'status': 201,
                    'data': serializer_result.data,
                })

            return Response({
                'status': 400,
                'data': serializer.errors
            })
        except Exception as e:
            return Response({
                'status': 400,
                'data': "Xato "+str(e)
            })


# Mijoz qo'shgan pochta e'lonini to'liq ko'rish
class DeliveryGetView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request):
        """
        Mijoz pochta e'lonini to'liq ko'rish

        Yo'lovchi e'lonini ko'rishimiz uchun so'rov tanasiga id kalitiga ko'rish kerak bo'lgan elonni idsi beriladi
        """
        try:
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            user_delivery = Delivery.objects.get(user=user, id=request.data['id'])
            serializer = DeliveryGetSerializer(user_delivery, many=False)
            return Response({
                'status': 200,
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 404,
                'data': "Xato e'lon mavjud emas! Yoki ma'lumotlar to'g'ri kelmadi "+str(e)
            })

# Mijoz qo'shgan e'lonini o'zgartirish
class DeliveryPutView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(request_body = DeliveryPutSerializer)
    def put(self, request):
        """
        Mijoz pochta e'lonini o'zgartirish

        Faqat holati o'zgartiriladi ya'ni agar elon qabul qilinsa yoki bekor qilinsa
        status False ga. Agar haydovchi qabul qilsa found Ture ga o'zgartiriladi.
        """
        try:
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            user_delivery = Delivery.objects.get(user=user, id=request.data['id'])
            serializer = DeliveryPutSerializer(user_delivery, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'data': serializer.data
                })

            return Response({
                'status': 400,
                'data': serializer.errors
            })
        except Exception as e:
            return Response({
                'status': 400,
                'data': "Xatolik "+str(e)
            })


































#
