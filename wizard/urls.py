from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('wizard_tech_explorer/', tech, name='tech'),
    path('tech_field/<int:id>/', field_detail, name='field_detail'),
    path( 'programming_language/<int:id>/', language_detail, name='language_detail'),
    path('blog/', blog, name='blog'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('subscribe/', subscribe, name='subscribe'),
    path('inquiry/', inquiry, name='inquiry'),
    path('inquiry/confirm/', inquiry_confirm, name='inquiry_confirm'),
    path('inquiry/success/', inquiry_success, name='inquiry_success'),
    path('download/pdf/<int:post_id>/', download_pdf, name='download_pdf'),
    path('download/pdf/<int:field_id>/', download_field_pdf, name='download_field_pdf'),
    path('test-404/', test_404),


]
