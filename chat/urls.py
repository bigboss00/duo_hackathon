from django.urls import path
from .views import message_list, user_list
urlpatterns = [
    path('messages/<int:sender>/<int:receiver>/', message_list, name='message-detail'),
    path('messages/', message_list, name='message-list'),
    path('users/<int:pk>/', user_list, name='user-detail'),
    path('users/', user_list, name='user-list'),
]
