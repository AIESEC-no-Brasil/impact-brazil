from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'api'
urlpatterns = [
    path('entities/', views.EntityList.as_view()),
    path('lcs/', views.LCList.as_view()),
    path('lcs/<int:pk>/', views.LCDetails.as_view()),
    path('subproducts/', views.SubproductList.as_view()),
    path('subproduct/<int:gis_id>/', views.SubproductDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('sdgs/', views.SDGList.as_view()),
    path('sdg/<int:number>', views.SDGDetail.as_view()),
    path('entity_partners/', views.EntityPartnerList.as_view()),
    path('entity_partners/<int:pk>/', views.EntityPartnerDetails.as_view()),
    path('opportunities/', views.OpportunityList.as_view()),
    path('login/', views.Login.as_view()),
    path('apply/', views.Apply.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
