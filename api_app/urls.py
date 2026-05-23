from django.urls import path
from api_app.views import *

urlpatterns = [
    path('student-create-list/', StudentCreateListAPI.as_view(), name="student_create_list"),
    path('student-detail/<str:t_id>/', StudentDetailListAPI.as_view(), name="student_detail"),
]
