from django.urls import path
from myapp.views import employee, index

urlpatterns = [
    path('', index, name='index'),  
    path('employee/', employee, name='employee'),  
]
