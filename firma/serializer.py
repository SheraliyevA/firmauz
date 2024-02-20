from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from .models import *
from django.utils.translation import gettext_lazy as _


class MahsulotSerializer(ModelSerializer):
    class Meta:
        model=Mahsulot
        fields=[
            "id",
           "mahsulot_id",
            'mahsulot_nomi' 
        ]

class Ishturi_or_BolimSerializer(ModelSerializer):
    class Meta:
        model=Ishturi_or_Bolim
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
    ish_turi=Ishturi_or_BolimSerializer()
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
