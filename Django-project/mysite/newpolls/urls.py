from django.urls import path
from . import views

urlpatterns = [
    path('' , views.new_index , name='new_index'),
    path('form',views.create_view , name = 'create_view'),
    path('viewform',views.list_view , name = 'list_view'),
    path('updateform<int:id>',views.update_view , name = 'update_view')
]