from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from .models import *
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        user = User.objects.get(username=self.user.username)
        data['status'] = user.status
        data['id'] = user.id
        return data
    
class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(MyTokenRefreshSerializer, self).validate(attrs)
        data['refresh'] = attrs.get('refresh') 
        return data 


class UserSerializer(ModelSerializer):
    class Meta: 
        model=User
        fields=[
            "id",
            "username",
            "password",
            "status",
            "phone"

        ]
        write_only_fields = ('password')
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user


class MahsulotSerializer(ModelSerializer):
    class Meta:
        model=Mahsulot
        fields=[
            "id",
           "mahsulot_id",
            'mahsulot_nomi' 
        ]

class Ishturi_Serializer(ModelSerializer):
    class Meta:
        model=Ishturi
        fields=[
            "id",
            "name",
            "ish_id"
        ]

class XodimSerializer(ModelSerializer):
    class Meta:
        model=Xodim
        fields=[
            "id",
            "status",
            "ism",
            "familiya",
            "phone",
            "ish_turi",
           "id_raqam"
        ]


class XodimGetSerializer(ModelSerializer):
    ish_turi=Ishturi_Serializer()
    class Meta:
        model=Xodim
        fields=[
            "id",
            "status",
            "ism",
            "familiya",
            "phone",
            "ish_turi",
            "id_raqam"
        ]

class XatoSerializer(ModelSerializer):
    class Meta:
        model=Xato
        fields=[
            "id",
            "xato_id",
            "problem"
         ]
        
class MissedSerializer(ModelSerializer):
    class Meta:
        model=Workinspection
        fields=[
            "id",
            "xodim_id",
            "xato_id",
            "xato_soni",
            "yaroqli_product_soni",
            "ish_vaqti",
            "created",
            "updated",
            "izoh",
            "user_id",
            "mahsulot_id"
        ]

class MissedGetSerializer(ModelSerializer):
    xodim_id=XodimSerializer()
    xato_id=XatoSerializer()
    mahsulot_id=MahsulotSerializer()
    class Meta:
        model=Workinspection
        fields=[
            "id",
            "xodim_id",
            "xato_id",
            "xato_soni",
            "yaroqli_product_soni",
            "ish_vaqti",
            "created",
            "updated",
            "izoh",
            "user_id",
            "mahsulot_id"
        ]

class BulimSerializer(ModelSerializer):
    class Meta:
        model=Bulim
        fields=[
            'id',
            'bolim_nomi',
            'bolim_id',
           "bolim_rahbari"
        ]
