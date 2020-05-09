from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Student
from .models import User
from .serializers import StudentSerializer
from .serializers import LibrarianSerializer
from .permission import UpdateOwnProfile


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = UpdateOwnProfile

    filter_backends = (filters.SearchFilter, )
    search_fields = ('first_name', 'email', )


class LibrarianViewSet(viewsets.ModelViewSet):
    serializer_class = LibrarianSerializer
    queryset = User.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = UpdateOwnProfile

    filter_backends = (filters.SearchFilter, )
    search_field = ('first_name', 'email', )


class LoginViewSet(viewsets.ViewSet):
    """ check email and password and return authtoken """

    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)

