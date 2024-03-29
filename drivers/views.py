from . serializer import RatingSerializer, RatingGetSerializer, DriverSerializer, DriverCartSerializer, DriverGetSerializer, DriverCartGetSerializer, DriverCartPutSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Driver, DriverCart, Rating
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from users.models import User
from drivers.models import Driver, DriverCart
from rest_framework.renderers import JSONRenderer

class DriverRatingGet(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def get(self, request):
        """
        Haydovchiga qo'yilgan baholar ro'yxati

        --
        """
        try:
            driver_comments = Rating.objects.filter(user=request.data['user'])
            serializer = RatingGetSerializer(driver_comments, many=True)
            if driver_comments.exists():
                driver_rating = DriverCart.objects.filter(driver__user=request.data['user']).last().rating
                return Response({
                    'status': 200,
                    'rating': driver_rating,
                    'data': serializer.data
                })
            return Response({
                'status': 404,
                'data': "Ushbu haydovchiga baho berilmagan"
            })
        except Exception as e:
            return Response({
                'status': 400,
                'data': "Xatolik "+str(e)
            })

class DriverRatingPost(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    @swagger_auto_schema(request_body = RatingSerializer)
    def post(self, request):
        """
        Haydovchiga yo'lovchi baho berishi


        -----
        """
        try:
            serializer = RatingSerializer(data = request.data)
            user = User.objects.get(id=request.data['user'])
            if serializer.is_valid():
                serializer.save(user=user)
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
                'data': "Xatolik "+str(e)
            })

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
                    # Agar haydovchida elon bo'lsa boshqa e'lon qo'shish imkoniyati bo'lmaydi
                    # bitta haydovchi bitta elon qo'shishi mumkin
                    return Response({
                        'status': 400,
                        'error': "Ushbu foydalanuvchida e'lon mavjud"
                    })
                serializer.save(user=user)
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
                'data': str(e)
            })

# Haydovchi elonini o'zgartirish
class DriverPutApiView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    @swagger_auto_schema(request_body = DriverSerializer)
    def put(self, request):
        try:
            user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
            user = User.objects.get(id=user_id)
            user_driver = Driver.objects.get(user=user)
            serializer = DriverSerializer(user_driver, data=request.data)
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
                'status': 404,
                'data': "Xatolik "+str(e)
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
            return Response({
                'status': 400,
                'data': serializer.errors
            })

        except Exception as e:
            return Response({
                'status': 400,
                'error': "Avtorizatsiydan o'tmadi. Yoki faol e'lon mavjud emas! "+str(e)
            })

# Haydovchi qidiruvga e'lon berish ishga chiqaman bosilganda
class DriverCartPostApiView(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body = DriverCartSerializer)
    def post(self, request, format=None):
        from django.db.models import Sum
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
                user_rating = Rating.objects.filter(user=user).aggregate(Sum('rating_clean'), Sum('rating_talk'), Sum('rating_time'))
                if user_rating['rating_clean__sum'] == None or user_rating['rating_talk__sum'] == None or user_rating['rating_time__sum'] == None:
                    total_sum_rating = 0.0
                else:
                    total_sum_rating = (user_rating['rating_clean__sum'] + user_rating['rating_talk__sum'] + user_rating['rating_time__sum']) / (3 * Rating.objects.filter(user=user).count())
                if DriverCart.objects.filter(driver=driver, status=True).exists():
                    DriverCart.objects.filter(driver=driver, status=True).update(status=False)
                serializer.save(driver=driver, rating="%0.2f" % total_sum_rating)
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
                'data': "Xatolik: " + str(e)
            })


# haydovchini qidiruvga bergan e'lonini o'ziga ko'rsatish
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
            if DriverCart.objects.filter(driver__user=user_id, status=True).exists():
                driver = DriverCart.objects.get(driver__user=user_id, status=True)
                print('==', driver)
                serializer = DriverCartGetSerializer(driver)
                return Response({
                    'status': 200,
                    'data': serializer.data
                })
            return Response({
                'status': 404,
                'data': "Bu foydalanuvchida faol e'lon yo'q!"
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error': "Xatolik "+str(e)
            })
