from django.urls import path
from .views import home_view,contact_view,blog_view,BlogDetailView ,portfolio_view,team_view,service_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('contact/',contact_view,name='contact-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('team/',team_view,name='team-page'),
    path('service/',service_view,name='service-page'),
    path('blogs/',blog_view,name='blog-page'),
    path('blog/<slug:slug>/',BlogDetailView.as_view(),name='blog-detail-page')

]
