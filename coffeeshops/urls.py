from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^signup/$',
        TemplateView.as_view(template_name='signup.html'),
        name='signup'),
    url(r'^businesses/(?P<slug>[-\w]+)/$', views.business_detail, name='business_detail'),
    url(r'^businesses/(?P<slug>[-\w]+)/edit/$', views.edit_business, name='edit_business'),
    url(r'^admin/', admin.site.urls),
]
