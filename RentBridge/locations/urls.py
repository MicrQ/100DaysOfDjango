from django.urls import path
from .views import (
    ListOrCreateLocationTypeView,
    RetrieveUpdateDestroyLocationTypeView
)


urlpatterns = [
    path('location_types/', ListOrCreateLocationTypeView.as_view(),
         name='location_types'),
    path('location_types/<str:pk>/',
         RetrieveUpdateDestroyLocationTypeView.as_view(),
         name='location_type'),
]
