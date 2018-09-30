# -*- coding: utf-8 -*-
from rest_framework import generics
from models import *
from serializers import *
from rest_framework import permissions
from rest_framework.exceptions import APIException, status

class MyException(APIException):
    def __init__(self, detail="未定义", status_code=status.HTTP_400_BAD_REQUEST):
        self.detail = detail
        self.status_code = status_code

class WebsiteAllList(generics.ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        comment = self.request.data.get('comment')
        website = Website.objects.filter(comment=comment)
        if len(website) > 0:
            print("已存在")
            raise MyException(u"已存在该名称")
        print("到这了")
        serializer.save()

    def get_queryset(self):
        queryset = Website.objects.all().order_by('id')
        return queryset