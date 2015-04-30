from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.myapp.views.base', name='base'),
    url(r'^login/','mysite.myapp.views.log', name='log'),
    url(r'^form/(?P<subject_id>[a-z]*)','mysite.myapp.views.form', name='form'),
    url(r'^finish/','mysite.myapp.views.completed', name='completed'),
    url(r'^second/','mysite.myapp.views.second', name='second'),
    url(r'^store/','mysite.myapp.views.store', name='store'),
    url(r'^sub/','mysite.myapp.views.sub', name='sub'),
    url(r'^logout/','mysite.myapp.views.logout1', name='logout1'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('django.contrib.auth.urls')),
)
