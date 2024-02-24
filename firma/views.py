from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser

class SignUpView(APIView):
    parser_classes = [JSONParser, MultiPartParser]
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        user = User.objects.all()
        serializers = UserSerializer(user, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class SignUpDetail(APIView):
    parser_classes = [JSONParser, MultiPartParser]
    permission_classes = [permissions.AllowAny]
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            ser = UserSerializer(user)
            return Response(ser.data)
        except:
            return Response({'{}': "bu id xato"})

    def patch(self, request, id):
        user = User.objects.get(id=id)
        ser = UserSerializer(user, data = request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class Mahsulot_view(APIView):
    def get(self,request):
        user=Mahsulot.objects.all()
        serializer=MahsulotSerializer(user,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MahsulotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        count = Mahsulot.objects.all().delete()
        return Response({'message': '{} Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
     
class MahsulotDetail(APIView):
     
     def delete(self,request,id):
        count = Mahsulot.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Mahsulot.objects.get(id=id)
        serializers=MahsulotSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
     
     def patch(self, request, id):
         ishturi=Mahsulot.objects.get(id=id)
         serializers = MahsulotSerializer(ishturi, data=request.data, partial=True)
         if serializers.is_valid():
             serializers.save()
             return Response(status=status.HTTP_201_CREATED)
         return Response(status=status.HTTP_400_BAD_REQUEST)
    
class Ishturi(APIView):
    
    def get(self,request):
        user=Ishturi.objects.all()
        serializer=Ishturi_Serializer(user,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Ishturi_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        count = Ishturi.objects.all().delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
 
class IshDetail(APIView):
     
     def delete(self,request,id):
        count = Ishturi.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Ishturi.objects.get(id=id)
        serializers=Ishturi_Serializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
     
     def patch(self, request, id):
         ishturi=Ishturi.objects.get(id=id)
         serializers = Ishturi_Serializer(ishturi, data=request.data, partial=True)
         if serializers.is_valid():
             serializers.save()
             return Response(status=status.HTTP_201_CREATED)
         return Response(status=status.HTTP_400_BAD_REQUEST)


class Xato_view(APIView):
    
    def get(self,request):
        user=Xato.objects.all()
        serializer=XatoSerializer(user,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = XatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    def delete(self,request):
        count = Xato.objects.all().delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class XatoDetail(APIView):
     
     def delete(self,request,id):
        count = Xato.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Xato.objects.get(id=id)
        serializers=XatoSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
     
      
     def patch(self, request, id):
        xato = Xato.objects.get(id=id)
        serializers = XatoSerializer(xato, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

class Missed_view(APIView):
    def get(self,request):
        user=Workinspection.objects.all()
        serializer=MissedGetSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = MissedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request):
        count = Workinspection.objects.all().delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class MissedDetail(APIView):
    def get(self,request,id):
        data=Workinspection.objects.get(id=id)
        serializers=MissedSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    
    def delete(self,request,id):
        count = Workinspection.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, id):
        missed = Workinspection.objects.get(id=id)
        serializers = MissedSerializer(missed, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

class Xodim_view(APIView):
    
    def get(self, request):
        xodim=Xodim.objects.all()
        serializers=XodimGetSerializer(xodim,many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = XodimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request):
        count = Xodim.objects.all().delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class XodimDetail(APIView):
     
     def delete(self,request,id):
        count = Xodim.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Xodim.objects.get(id=id)
        serializers=XodimSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
     
     def patch(self, request, id):
        xodim = Xodim.objects.get(id=id)
        serializers = XodimSerializer(xodim, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)
     
    
     
class Bulim_View(APIView):
    def get(self,request):
        bulim=Bulim.objects.all()
        serializers=BulimSerializer(bulim,many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializers = BulimSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request):
        count = Bulim.objects.all().delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class Bulim_Detail(APIView):
     
     def delete(self,request,id):
        count = Bulim.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Bulim.objects.get(id=id)
        serializers=BulimSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
     
     def patch(self, request, id):
        bulim = Bulim.objects.get(id=id)
        serializers = BulimSerializer(bulim, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)