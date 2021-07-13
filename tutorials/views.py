from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from tutorials.models import Tutorial
from tutorials.serializers import TutorialsSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)

        tutorials_serializer = TutorialsSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_detail(request):
    print(request.method)
    return JsonResponse(TutorialsSerializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def tutorial_list_published(request):
    print(request.method)
    return JsonResponse(TutorialsSerializer.data, status=status.HTTP_200_OK)
