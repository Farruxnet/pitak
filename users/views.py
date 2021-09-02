from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from . serializer import UserSerializer, UserProfileSerializer, UserUpdateProfileSerializer
from rest_framework.response import Response
from . models import User
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer

class Register(APIView):
    renderer_classes = [JSONRenderer]
    @swagger_auto_schema(request_body = UserSerializer)
    def post(self, request):
        """
        Foydalanuvchini ro'yxatga olish

        ---
        """
        try:
            serializer = UserSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(phone_number = serializer.data['phone_number'])
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'status': 200,
                    'phone_number': serializer.data['phone_number'],
                    'token': str(token)
                })

            if User.objects.filter(phone_number=serializer.data['phone_number']).exists():
                token, _ = Token.objects.get_or_create(user=User.objects.get(phone_number = serializer.data['phone_number']))
                return Response({
                    'status': 200,
                    'phone_number': serializer.data['phone_number'],
                    'token': str(token)
                })

            return Response({
                'status': 400,
                'error': serializer.errors
            })
        except Exception as e:
            return Response({
                'status': 400,
                'error':str(e)
            })


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    parser_classes = (FormParser, MultiPartParser)
    def get(self, request):
        """
        Foydalanuvchini shahsiy ma'lumotlarini olish

        ---
        """
        try:
            if request.META['HTTP_AUTHORIZATION'].split(' ')[1]:
                user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
                user = User.objects.get(id=user_id)
                serializer = UserProfileSerializer(user)
                return Response({
                    'status': 200,
                    'data': serializer.data
                })
            return Response({
                'status': 400,
                'error': serializer.errors
            })
        except Exception as e:
            return Response({
                'status': 401,
                'error': "Avtorizatsiyadan o'tmadi! Token xato "+str(e)
            })


    @swagger_auto_schema(request_body=UserUpdateProfileSerializer)
    def put(self, request):
        """
        Foydalanuvchini shahsiy ma'lumotlarini o'zgartirish

        ---
        """
        try:
            if request.META['HTTP_AUTHORIZATION'].split(' ')[1]:
                user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
                user = User.objects.get(id=user_id)
                serializer = UserUpdateProfileSerializer(user, data=request.data)
                if serializer.is_valid():
                    if request.data.get('profile_photo'):
                        serializer.save(profile_photo=request.data.get('profile_photo'))
                    else:
                        serializer.save()
                    return Response({
                        'status': 200,
                        'data': serializer.data
                    })
                return Response({
                    'status': 400,
                    'error': serializer.errors
                })

            return Response({
                'status': 401,
                'error': "Avtorizatsiyadan o'tmadi! Token xato"
            })
        except Exception as e:
            return Response({
                'status': 401,
                'error': "Avtorizatsiyadan o'tmadi! "+str(e)
            })


























# s
