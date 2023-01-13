from django.urls import path
from .views import InfoGet


# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('get_info_sales/', InfoGet.as_view())
]