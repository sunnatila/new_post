from django.urls import path
from .views import HomeListView, FootListView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('foot/', FootListView.as_view(), name='foot')
]


