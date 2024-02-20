from django.urls import path
from .views import *

urlpatterns=[
    path('api/tutorials',Mahsulot_view.as_view()),
    path('api/tutorials/<int:id>',MahsulotDetail.as_view()),
    path('api/ish',Ishturi.as_view()),
    path('api/ish/<int:id>',IshDetail.as_view()),
    path('api/xodim',Xodim_view.as_view()),
    path('api/xodim/<int:id>',XodimDetail.as_view()),
    path('api/xato',Xato_view.as_view()),
    path('api/xato/<int:id>',XatoDetail.as_view()),
    path('api/missed',Missed_view.as_view()),
    path('api/missed/<int:id>',MissedDetail.as_view()),
    path('api/bulim',Bulim_View.as_view()),
    path('api/bulim/<int:id>',Bulim_Detail.as_view())
    
]