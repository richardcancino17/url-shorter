from rest_framework import generics, status
from django.shortcuts import redirect
from rest_framework.response import Response
from .serializers import *


class CreateUrlShorterAPIView(generics.CreateAPIView):
    serializer_class = CreateUrlShorterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,
                                         context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SeeUrlShorterAPIView(generics.ListAPIView):
    serializer_class = SeeUrlShorterSerializer

    def get_queryset(self):
        return UrlShorter.objects.all()


class GetTimesOpenUrlShorterAPIView(generics.RetrieveAPIView):
    serializer_class = UrlShorterSerializer

    def get_object(self):
        code_shorter = self.kwargs.get('code_shorter')
        url = UrlShorter.objects.get(code_shorter=code_shorter)
        url.times_used += 1
        url.save()
        return url

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        if object:
            return redirect(object.link_original)
        else:
            return Response(
                {
                    'object': 'error',
                    'message': 'Shorter link does not exist',
                    'code': 'A00-001'
                },
                status=status.HTTP_404_NOT_FOUND)
