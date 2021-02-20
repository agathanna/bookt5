from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path ('search/', views.search, name='search'),
    path ('add/', views.add, name='add'),
    path ('upload/', views.upload, name= 'upload'),
    path ('', views.autocomplete, name= 'autocomplete'),
    path('plot_summary_autocomplete/', views.plot_summary_autocomplete, name='plot_symmary_autocomplete'),
         
]

