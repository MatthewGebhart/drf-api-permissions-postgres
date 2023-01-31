from rest_framework import generics
from .serializers import OtterSerializer
from .models import Otter


class OtterList(generics.ListCreateAPIView):
    queryset = Otter.objects.all()
    serializer_class = OtterSerializer


class OtterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Otter.objects.all()
    serializer_class = OtterSerializer

