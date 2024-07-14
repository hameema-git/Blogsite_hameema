from .views  import *
from django.urls import path,include
urlpatterns = [
    
    path('home/',home,name='pg1'),
    path('create/',create,name='pg2'),
    path('viewall/',viewall,name='pg3'),
    path('delete/<int:pk>',TaskDeleteView.as_view(),name='pg4'),
    path('detail/<int:pk>',TaskDetailview.as_view(),name="pg5"),
    path('update/<int:pk>',TaskUpdateView.as_view(),name="pg6"),
    path('',login,name='login'),
    path('logout/',logout,name='logout')
]
