from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken



from .models import User
import re

# Create your views here.

@api_view(['GET'])
def welcomeTest(request):
    print('server working!')
    return Response({ 'message':'Server working!'})


@api_view(['post'])
def register(request):
    data = request.data

    required_fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone_number']
    for field in required_fields:
        if field not in data or not data[field].strip():
            return Response({ "error": f"{field} is required." }, status=400)

    if data['password'] != data['confirm_password']:
        return Response({ "error": "Passwords do not match." }, status=400)

    if not re.match(r'^(010|011|012|015)\d{8}$', data['phone_number']):
        return Response({ "error": "Invalid Egyptian phone number." }, status=400)
    
    obj = UserSerializer(data=data)
    if obj.is_valid():
        obj.save()
    else:
         return Response(obj.errors, status=400)

    return Response({ "message" : "User Registered" , "User" : obj.data }, status=201)


@api_view(['POST'])
def loginUser(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password are required."}, status=400)


    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials."}, status=401)

    if user.password != password:
        return Response({"error": "Invalid credentials."}, status=401)

    refresh = RefreshToken.for_user(user)

    return Response({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": user.phone_number
        },
        "tokens": {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
    }, status=200)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_route(request):
    return Response({"message": f"Hello {request.user.first_name}, you're authenticated!"})

@api_view(['POST'])
def custom_token_refresh(request):
    refresh_token = request.data.get("refresh")
    
    if not refresh_token:
        return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        token = RefreshToken(refresh_token)
        user_id = token["user_id"]

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found", "code": "user_not_found"}, status=status.HTTP_404_NOT_FOUND)

        new_access = str(token.access_token)

        return Response({
            "access": new_access
        })

    except TokenError:
        return Response({"detail": "Invalid or expired token", "code": "token_invalid"}, status=status.HTTP_401_UNAUTHORIZED)