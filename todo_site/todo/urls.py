from django.urls import path

from .views import (
    index,
    remove
)

urlpatterns = [
    #home page
    path('', index, name="todo"),
    #delete
    path('del/<str:item_id>', remove, name='del')
]