from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response

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
    
    def patch(self,request):
        serializer = MahsulotSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 
 
class MahsulotDetail(APIView):
     
     def delete(self,request,id):
        count = Mahsulot.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Mahsulot.objects.get(id=id)
        serializers=MahsulotSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
        


    
class Ishturi(APIView):
    
    def get(self,request):
        user=Ishturi_or_Bolim.objects.all()
        serializer=Ishturi_or_BolimSerializer(user,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Ishturi_or_BolimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        count = Ishturi_or_Bolim.objects.all().delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    def patch(self,request):
        serializer = Ishturi_or_BolimSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 
 
 
class IshDetail(APIView):
     
     def delete(self,request,id):
        count = Ishturi_or_Bolim.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Ishturi_or_Bolim.objects.get(id=id)
        serializers=Ishturi_or_BolimSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)

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
    
    def patch(self,request):
        serializer = XatoSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    
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
    
    def patch(self,request):
        serializer = MissedSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    
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


class Xodim_view(APIView):
    
    def get(self, request):
        xodim=Xodim.objects.all()
        serializers=XodimGetSerializer(xodim,many=True)
        return Response(serializers.data)

    # def post(self, request):
    #     serializer = XodimSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def patch(self,request):
    #     serializer = XodimSerializer(request.user, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED) 
    #     return Response(status=status.HTTP_400_BAD_REQUEST) 

    
    # def delete(self,request):
    #     count = Xodim.objects.all().delete()
    #     return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

class XodimDetail(APIView):
     
     def delete(self,request,id):
        count = Xodim.objects.get(id=id).delete()
        return Response({'message': '{}  Ma\'lumot o\'chirildi!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

     
     def get(self,request,id):
        data=Xodim.objects.get(id=id)
        serializers=XodimSerializer(data)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
     
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
    
    def patch(self,request):
        serializers = BulimSerializer(request.user, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(status=status.HTTP_201_CREATED) 
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    
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
