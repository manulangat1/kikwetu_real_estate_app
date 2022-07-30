from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import Property, PropertyViews

class PropertySerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    class Meta:
        model = Property
        fields = [
            'id',
            'user',
            'title',
            'description',
            'price',
            'tax',
            'country',
            'property_type',
            'advert_type',
            'cover_photo',
            'photo1',
            'photo2',
            'photo3',
            'photo4',
            'published_status',
            'views',
            'created_at',
            'updated_at',
        ]
    def get_user(sef, obj):
        return obj.user.username
    # def to_representation(self, instance):
    #     return super().to_representation(instance

class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        # fields = '__all__'
        exclude =  ["updated_at", "pkid" ]

class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        exclude =  ["updated_at", "pkid" ]
        # fields = '__all__'
        # read_only_fields = ['property']
        # extra_kwargs = {
        #     'property': {'required': True}
        # }

# class PropertyViewCreateSerializer(serializers.ModelSerializer):
