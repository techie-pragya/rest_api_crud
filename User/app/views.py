

# Create your views here.
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from app.models import AppUser
from app.serializer import AppUserSerializer
from rest_framework.decorators import api_view





@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        app = AppUser.objects.all()
        
        username = request.GET.get('Username', None)
        if username is not None:
            app = app.filter(title__icontains=Username)
        
        app_serializer = AppUserSerializer(app, many=True)
        return JsonResponse(app_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        app_data = JSONParser().parse(request)
        app_serializer = AppUserSerializer(data=app_data)
        if app_serializer.is_valid():
            app_serializer.save()
            return JsonResponse(app_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    elif request.method == 'DELETE':
        count = AppUser.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    app = AppUser.objects.get(pk=pk)
    if request.method == 'GET':
        app_serializer =AppUserSerializer(app) 
        return JsonResponse(app_serializer.data) 

    elif request.method == 'PUT': 
        app_data = JSONParser().parse(request) 
        app_serializer = AppUserSerializer(app, data=app_data) 
        if app_serializer.is_valid(): 
            app_serializer.save() 
            return JsonResponse(app_serializer.data) 
        return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        app.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




