from django.urls import path,include

from .views import (
    index,
    remove,
    user_login,
)

urlpatterns = [
    path('main', index, name="todo"),
    path('del/<str:item_id>', remove, name='del'),
    path('login', user_login, name='login'),
]
