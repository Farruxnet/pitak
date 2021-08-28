from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from . serializer import UserSerializer, UserProfileSerializer
from rest_framework.response import Response
from . models import User
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

class Register(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        try:
            serializer = UserSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                user = User.objects.get(phone_number = serializer.data['phone_number'])
                token, _  = Token.objects.get_or_create(user=user)
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

            return Response(serializer.errors)
        except Exception as e:
            print(e)
            print(request.data)

            return Response({
                'status': 503,
                'message': 'Error'
            })


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            if request.META['HTTP_AUTHORIZATION'].split(' ')[1]:
                user_id = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user_id
                user = User.objects.get(id=user_id)
                serializer = UserProfileSerializer(user)
                return Response(serializer.data)
            return Response({
                'status': 403,
                'message': "Invalid token"
            })
        except Exception as e:
            print('==', e)
            print('==2', request.data)
            return Response({
                'status': 503,
                'message': "Authorization error. Invalid token"
            })
    @swagger_auto_schema(request_body=UserProfileSerializer)
    def put(self, request):
        try:
            if request.data['Authorization'].split(' ')[1]:
                user_id = Token.objects.get(key=request.data['Authorization'].split(' ')[1]).user_id
                user = User.objects.get(id=user_id)
                serializer = UserProfileSerializer(user, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)

            return Response({
                'status': 403,
                'message': "Invalid token"
            })
        except Exception as e:
            return Response({
                'status': 403,
                'message': "Invalid value"
            })


























# s
