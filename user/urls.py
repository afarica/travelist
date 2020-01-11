from django.urls import path
from .views import index_page, about_page


urlpatterns = [
    path('', index_page, name='index'),
    path('about/', about_page, name='about'),

]
