from ..models import BaseUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['username']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['id', 'username']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = BaseUser
        fields = [
            'username',
            'password',
            'password2'
        ]
        extra_kwargs = {
            'password1': {'write_only': True}
        }

    def save(self, **kwargs):
        user = BaseUser(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password1': 'password1 and password2 must be the same.'})
        user.set_password(password)
        user.save()
        return user


# class LoginSerializer(serializers.ModelSerializer):
