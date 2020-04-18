from django.urls import path
from . import views
from .views import (CoupanListView,
                    CoupanDetailView,
                    CoupanCreateView,
                    CoupanUpdateView,
                    CoupanDeleteView,
                    UserCoupanListView)

urlpatterns = [
    path('', CoupanListView.as_view(), name='coupan-home'),
    path('user/<str:username>', UserCoupanListView.as_view(), name='user-coupan'),
    path('coupan/<int:pk>/', CoupanDetailView.as_view(), name='coupan-detail'),
    path('coupan/new/', CoupanCreateView.as_view(), name='coupan-create'),
    path('coupan/<int:pk>/update/', CoupanUpdateView.as_view(), name='coupan-update'),
    path('coupan/<int:pk>/delete/', CoupanDeleteView.as_view(), name='coupan-delete'),
]
