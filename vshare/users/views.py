# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#######################################
from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from users.serializers import *
from groups.serializers import GroupSerializer
from rest_framework.authtoken.models import Token

from users.models import *
from rest_framework import generics

from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
		CreateAPIView,
		DestroyAPIView,
		ListAPIView,
		UpdateAPIView,
		RetrieveAPIView,
		RetrieveUpdateAPIView
	)

from rest_framework.permissions import (
		AllowAny,
		IsAuthenticated,
		IsAdminUser,
		IsAuthenticatedOrReadOnly,
	)
import requests


class Registration(generics.ListCreateAPIView):
	permission_classes = [AllowAny]
	queryset = Account.objects.all()
	serializer_class = RegistrationSerializer

class UserLogin(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer

	def post(self,request,*args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.validated_data['user']
			token = Token.objects.get(user=user) 
			return Response(
				{
					'token': token.key, 
					'username':user.username,
					'email': user.email
				}, status=HTTP_200_OK
			)

		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UserByUsername(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'username'
    permission_classes = [AllowAny]


class EditProfile(generics.RetrieveUpdateDestroyAPIView):
	def check(self):
		user = self.request.user
		if Account.objects.get(username=user).photo:
			response = create_presigned_url('vshare-profile-images', user)
			if response is not None:
				http_response = requests.get(response)
				Account.objects.get(username=user).photo = True
				return response
				print(response)
			else:
				exit(1)	
		else:
			response = create_presigned_post('vshare-profile-images', user)
			if response is not None:
				http_response = requests.post(response['url'], data=response['fields'], files=files)
				logging.info(f'File upload HTTP status code: {http_response.status_code}')
			else:
				exit(1)

	permission_classes = [AllowAny]
	queryset = Account.objects.all()
	lookup_field = 'username'
	serializer_class = EditProfileSerializer



# # Generate a presigned S3 POST URL
# object_name = 'OBJECT_NAME'
# response = create_presigned_post('BUCKET_NAME', object_name)
# if response is None:
#     exit(1)

# # Demonstrate how another Python program can use the presigned URL to upload a file
# with open(object_name, 'rb') as f:
#     files = {'file': (object_name, f)}
#     http_response = requests.post(response['url'], data=response['fields'], files=files)


# # If successful, returns HTTP status code 204

		

