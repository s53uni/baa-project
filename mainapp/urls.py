from django.urls import path

from . import views

urlpatterns = [
    ### 진단 답변페이지
    # - http://127.0.0.1:8000/diagnosis_detail
    path('diagnosis_detail', views.diagnosis_detail),
    ### 진단 페이지
    # - http://127.0.0.1:8000/diagnosis
    path('diagnosis', views.diagnosis, name='diagnosis'),
    
    ### 메인 페이지
    # - http://127.0.0.1:8000/index/
    path('index/', views.main),
    # - http://127.0.0.1:8000/
    path('', views.main),
]
