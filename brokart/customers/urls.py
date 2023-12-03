
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('account',views.show_account,name='account'),
    path('logout',views.sign_out,name='logout'),
  
]
