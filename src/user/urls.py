from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register('student', views.StudentViewSet, )
router.register('librarian', views.LibrarianViewSet, )
router.register('login', views.LoginViewSet, basename='login')

urlpatterns = [
    url(r'', include(router.urls), )

]


