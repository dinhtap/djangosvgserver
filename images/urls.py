from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('images/<str:img_name>/', views.image, name='image'),
    path('myimages/', views.myimages, name='myimages'),
    path('myimages/<str:imagename>/', views.imageedit, name='imageedit'),
    path('myimages/<str:imagename>/addrectangle/', views.addrectangle, name='addrectangle'),
    path('myimages/delrectangel/<int:recid>', views.delrectangle, name='delrectangle')
]