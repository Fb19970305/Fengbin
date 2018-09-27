# -*- coding: utf-8 -*-
from rest_framework import generics
from models import *
from serializers import *
from rest_framework import permissions

class WebsiteAllList(generics.ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = Website.objects.all().order_by('id')
        return queryset