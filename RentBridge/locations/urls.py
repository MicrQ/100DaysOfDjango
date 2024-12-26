from django.urls import path
from .views import ListOrCreateLocationTypeView


urlpatterns = [
    path('location_types/', ListOrCreateLocationTypeView.as_view(),
         name='location_types'),
]
