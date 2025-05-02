from django.urls import path
from . import views 
urlpatterns=[
    path('',views.student_list,name='student_list'),
    path('student/<int:pk>/',views.student_detail,name='student_detail'),
    path('student/<int:pk>/pdf/',views.student_pdf,name='student_pdf')
]