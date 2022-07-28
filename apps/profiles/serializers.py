from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from apps.ratings.serializers import RatingSerializer
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer): 
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile 
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 
            'full_name',
             'country', 
            'about_me', 'profile_photo', 'phone_number'
            ,'reviews'
        ]

    def get_full_name(self, obj):
        first_name  = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return first_name + " " + last_name
    def get_reviews(self, obj):
        reviews =  obj.agent_review.all()
        return RatingSerializer(reviews, many=True).data
        # return RatingSerializer(obj.reviews.all(), many=True).data
    def to_representation(self, obj):
        representation = super(ProfileSerializer, self).to_representation(obj)
        if obj.top_agent:
            representation['top_agent'] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            'id', 'about_me', 'profile_photo', 'phone_number', 
            'country', 'city', 'is_seller',
            'is_buyer'
        ]