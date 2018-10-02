from rest_framework import generics
from serializers import *


class ElsaAllList(generics.ListCreateAPIView):
    queryset = Elsa.objects.all()
    serializer_class = ElsaSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        try:
            cloth_type = int(self.request.GET.get('cloth_type'))
            queryset = Elsa.objects.filter(cloth_type=cloth_type).order_by('id')
        except:
            queryset = Elsa.objects.all().order_by('id')
        return queryset