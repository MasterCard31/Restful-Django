
from django.urls import path
from . import views


urlpatterns = [
    path('series/', views.serie_list),
    path('series/<int:pk>/', views.serie_detail),
]


