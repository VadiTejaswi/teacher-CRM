from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.teach,name='all-teachers'),
    path("add/",views.add_teacher,name="adding"),
    path('edit/<str:id>/',views.edit_teacher,name="update"),
    path('delete/<str:id>/',views.deleted,name="deleteteach")
]