from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

tags_info = {
    
}
urlpatterns = patterns('myblog.views',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^$','indexinfo',{'template_name': 'index.html'}),
    ('^about/$','about'),
    ('^blog/$','blog_index'),
    (r'^article/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<blog_title>.*)/$','blog_body'),
    ('^time/$','time'),
    # (r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$','blog'),

)
urlpatterns += patterns('',
  url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.STATIC_ROOT }),
   )

