import profile
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ImageField(source="profile.profile_photo")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    top_seller = serializers.BooleanField(source="profile.top_seller")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields =  [
            'id', 'username', 'first_name', 'last_name', 'full_name', 'email', 'phone_number', 'profile_photo', 'country', 'city', 'top_seller', 'last_login'
        ]
                # fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login')
        # read_only_fields = ('id', 'date_joined', 'last_login')
        def get_first_name(self, obj):
            return obj.first_name.title()
        def get_last_name(self, obj):
            return obj.last_name.title()
        def to_representation(self, obj):
            representation = super(UserSerializer).to_representation(obj)
            if  obj.is_superuser:
                representation['is_admin'] = True
            return representation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [ 'id', 'username', 'first_name', 'last_name', 'email', 'password']
    