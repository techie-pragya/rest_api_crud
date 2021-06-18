from django.conf.urls import url 
from app import views 
 
urlpatterns = [ 
    url(r'^api/users$', views.user_list),
    url(r'^api/User/(?P<pk>[0-9]+)$', views.user_detail),
    
]