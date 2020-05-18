"""proABC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ABCapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',views.home, name='home'),
    path('register/', views.registerpage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('footer/',views.footerpage, name='footer'),
    path('mainbook/',views.mainBook, name='mainBook'),
    path('lobpics/',views.lob,name='lob'),
    path('prgoics/',views.pro,name='pro'),
    path('novpics/',views.nov,name='nov'),
    path('actionpics/',views.act,name='act'),
    path('support/',views.support,name='support'),
    path('readmore/',views.readmore,name='readmore'),
    path('contact/',views.contact,name='contact'),
    path('sorry/',views.sorry,name='sorry'),
    path('payment/',views.payment,name='payment'),
    path('paytm/',views.paytm,name='paytm'),
    path('gpay/',views.gpay,name='gpay'),
    path('ppay/',views.ppay,name='ppay'),
    path('ppal/',views.ppal,name='ppal'),

]
