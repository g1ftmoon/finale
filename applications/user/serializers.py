from rest_framework import serializers

from applications.account.admin import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'