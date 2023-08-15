"""
GamblingDj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
#from django.contrib import admin
from django.urls import path
from gambler import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    path('',views.pay, name = 'pay'),
    path('copy token/', views.copy_Token, name = 'ctoken'),
    path('enter token/', views.enter_Token, name = 'etoken'),
    path('toss/', views.toss, name = 'toss'),
   
    path('gambler/', views.gambler, name = 'gambler'),
    path('game-over/', views.game_over, name = 'game-over'),
    path('roll-dice/', views.roll_die, name = 'roll-dice'),
    path('dice/', views.dice, name = 'dice'),
    path('cashout/', views.cashout, name = 'cashout'),
    path('my-view/', views.myview, name = 'my-view'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
