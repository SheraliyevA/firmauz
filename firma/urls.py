from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns=[
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/<int:id>/', SignUpDetail.as_view(), name='signup_detail'),

   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('mahsulot/',Mahsulot_view.as_view()),
    path('mahsulot/<int:id>',MahsulotDetail.as_view()),
    path('ish_turi/',Ishturi.as_view()),
    path('ish_turi/<int:id>',IshDetail.as_view()),
    path('api/xodim',Xodim_view.as_view()),
    path('api/xodim/<int:id>',XodimDetail.as_view()),
    path('xatolar/',Xato_view.as_view()),
    path('xatolar/<int:id>',XatoDetail.as_view()),
    path('missed',Missed_view.as_view()),
    path('missed/<int:id>',MissedDetail.as_view()),
    path('bulim/',Bulim_View.as_view()),
    path('bulim/<int:id>',Bulim_Detail.as_view())
    
]