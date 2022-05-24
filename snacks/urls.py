from django.urls import path
from .views import AboutPageView, HomePageView, SnackListView, SnackDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('snacks/', SnackListView.as_view(), name='snacks'),
    path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail')
]