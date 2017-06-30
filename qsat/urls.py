from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^download/$', 'home.views.download', name='download'),
    url(r'^contact/$', 'home.views.team', name='team'), 
    url(r'^register/$', 'home.views.register', name='register'),
    url(r'^registercomplete/$', 'home.views.registercom', name='registercom'),
    # url(r'^rarara/$', 'home.views.registera', name='registera'),

    url(r'^admin/', include(admin.site.urls)),
]
