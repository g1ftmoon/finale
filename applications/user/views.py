from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.admin import User


class UserView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = request.user
        profile = User.objects.get(user=user.id)
        from applications.user.serializers import UserSerializer
        serializer = UserSerializer(profile, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)