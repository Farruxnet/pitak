from . serializer import CustomerGetSerializer, CustomerPutSerializer, CustomerPostSerializer, DriverCartGetAllSerializer
from . models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from users.models import User
from rest_framework.renderers import JSONRenderer
from drivers.models import Driver, DriverCart
from data.models import District, Province, Automobile, Deriction

# Mijoz haydovchi qidirish uchun ma'lumotlarni kiritish
class CustomerPostView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(request_body = CustomerPostSerializer)
    def post(self, request):
        """
        Mijoz haydovchi qidirish uchun ma'lumotlarni kiritish


        ---------
        """
        try:
            serializer = CustomerPostSerializer(data = request.data)
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            deriction_list = DriverCart.objects.filter(
                current_location=Province.objects.get(id=request.data['customer_current_province']),
                finish_location=Province.objects.get(id=request.data['customer_finish_province']),
                driver__automobile=Automobile.objects.get(id=request.data['automobile']),
                driver__district__in=[request.data['customer_finish_district']],
                empty_count__gte=request.data['passengers_count'],
                status=True
            ).order_by('rating')
            
            serializer_result = DriverCartGetAllSerializer(deriction_list, many=True)
            if Customer.objects.filter(user=user).exists():
                Customer.objects.filter(user=user).update(status=False)

            if serializer.is_valid():
                serializer.save(user=user)
                return Response({
                    'status': 201,
                    'data': serializer_result.data
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


# Yulovchida haydovchi qidirganda kiritgan ma'lumotlarini e'lonlarini ko'rish
class CustomerGetView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def get(self, request):
        """
        Yulovchida haydovchi qidirganda kiritgan ma'lumotlarini e'lonlarini ko'rish


        ------------
        """
        try:
            from rest_framework.pagination import PageNumberPagination
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            customer = Customer.objects.filter(user=user).order_by('-id')
            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(customer, request)
            serializer = CustomerGetSerializer(page, many=True)

            return paginator.get_paginated_response({
                'status': 200,
                'data': serializer.data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'data': "Xato "+str(e)
            })

# mijoz haydovchi qidirganda kiritgan holatini o'zgartirish
class CustomerPutView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    @swagger_auto_schema(request_body = CustomerPutSerializer)
    def put(self, request):
        """
        Mijoz haydovchi qidirganda kiritgan elonini holatini o'zgartirish

        so'rov tanasida id kaliti va unga qiymat sifatida o'zgarishish kerak bo'lgan e'lon idsi beriladi
        """
        try:
            customer = Customer.objects.get(id=request.data['id'])
            serializer = CustomerPutSerializer(customer, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 201,
                    'data': serializer.data
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
