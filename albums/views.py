from .models import Album
from .serializers import AlbumSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

class AlbumPagination(PageNumberPagination):
    page_size = 2

class AlbumView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = AlbumPagination

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
