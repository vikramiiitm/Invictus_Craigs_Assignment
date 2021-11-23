from django.urls import path
from . import views
urlpatterns = [
    path('',views.DetailProfile.as_view())
]
