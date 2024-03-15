from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('login',views.userlogin, name=''),
    path('prod_details/<int:id>',views.prod_details,name='')
    # initializing <int:id> in the url pattern to ensure unique url pattern for each individual products details page
    # the path() function replaces the <int:id> with the id number of the particular product from databse 
]