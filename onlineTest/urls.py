from django.urls import path
from onlineTest.views import *

urlpatterns=[
    path('show-question/',question_info),
    path('save-question/',saveQuestion),
    path('new-question/',newQuestion),
    path('online-test/',test),
    path('login/',userLogin),
    path('logout/',userLogout),
    path('start-test/',startTest),
    path('result/',calculateResult),
]