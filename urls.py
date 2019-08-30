from django.conf.urls import url
from second_app import views

app_name = 'second_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact')
]
