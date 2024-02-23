from django.urls import path
from .views import SignUpView, CustomLoginView, activate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

]