from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import SmsSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . sms_service import sms_sender

class SmsView(APIView):
    VALIDATE_CLASS = None
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = SmsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            if sms_sender(serializer.data['phone_number'], serializer.data['code']):
                return Response({
                    'status': 200,
                    'code': serializer.data['code'],
                    'phone_number': serializer.data['phone_number']
                })

            return Response({
                'status': 400,
                'error': "Raqam xato ko'rsatildi!"
            })


        return Response({
            'status': 400,
            'error': serializer.errors
        })
