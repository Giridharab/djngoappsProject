# new
# from django.shortcuts import render
# from django.views.decorators.http import require_GET
#
# from .serializers import *
# from .models import *
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
#
# @api_view(['GET'])  # read
# def Nuggetlist(request):
#     nuggetobj = Nugget.objects.all()  # queryset
#     serializer = NuggetSerializer(nuggetobj, many=True)
#     return Response(serializer.data)
#
#
# # create
# @api_view(['POST'])
# def post_Nugget(request):
#     nuggetobj = Nugget.objects.all()  # queryset
#     serializer = NuggetSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# # Modify
# @api_view(['POST'])
# def Modify_Nugget(request, id):
#     nuggetobj = Nugget.objects.get(id=id)  # queryset
#     serializer = NuggetSerializer(instance=nuggetobj, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# # Delete
# @api_view(['DELETE'])
# def delete_Nugget(request, id):
#     nuggetobj = Nugget.objects.get(id=id)  # queryset
#     nuggetobj.delete()
#     return Response("Nugget is deleted successfully")
#
#
# # search
from django.views.generic import ListView

from .models import *
from django.shortcuts import render
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin


class Nuggetlist(GenericAPIView, ListModelMixin):
    queryset = Nugget.objects.all()
    serializer_class = NuggetSerializer

    def get(self, request):
        return self.list(request)


class Nuggetcreate(GenericAPIView, CreateModelMixin):
    queryset = Nugget.objects.all()
    serializer_class = NuggetSerializer

    def post(self, request):
        return self.create(request)


class Nuggetdis(GenericAPIView, RetrieveModelMixin):
    queryset = Nugget.objects.all()
    serializer_class = NuggetSerializer

    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)


class Nuggetup(GenericAPIView, UpdateModelMixin):
    queryset = Nugget.objects.all()
    serializer_class = NuggetSerializer

    def put(self, request, **kwargs):
        return self.update(request, **kwargs)


class Nuggetdel(GenericAPIView, DestroyModelMixin):
    queryset = Nugget.objects.all()
    serializer_class = NuggetSerializer

    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)


class NuggetSearchView(ListView):
    model = Nugget
    template_name = 'search_results.html'
    context_object_name = 'nuggets'

    def get_queryset(self):
        query = self.request.GET.get('query')  # Get the search query from the request

        # Perform the search using the icontains lookup
        queryset = super().get_queryset().filter(content__icontains=query)
        return queryset
