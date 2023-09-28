from django.urls import path
from .views import hello, HelloView, my_view, TemplIf, user_form

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('user/add/', user_form, name='user_form'),
]
