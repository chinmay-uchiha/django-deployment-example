from django.urls import path
from DemoApp import views
app_name='DemoApp'
urlpatterns=[
    path('staff/',views.staff,name='staff'),
    path('student/',views.student,name='student'),
    path('student_display/',views.student_display,name='student_display'),
]
