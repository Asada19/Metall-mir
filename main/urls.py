from django.urls import path
from .views import CallBackCreateAPIView, ContactsAPIView, SocialMediaAPIView


urlpatterns = [
    path('callbacks/', CallBackCreateAPIView.as_view(), name='callbacks'),
    path('contacts/', ContactsAPIView.as_view(), name='contacts'),
    path('social-media/', SocialMediaAPIView.as_view(), name='social-media')
]
