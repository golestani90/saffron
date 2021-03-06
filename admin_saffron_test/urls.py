from django.conf.urls import patterns, include, url
#from django.contrib import admin
#admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'admin_saffron_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'myapp.views.admin_parent', name='admin'),
    url(r'^admin/news/rss$', 'myapp.views.admin_news_rss', name='admin_news_rss'),
    url(r'^news/hand$', 'myapp.views.admin_news_hand', name='admin_news_hand'),
    url(r'^news/edit/rss$', 'myapp.views.admin_news_edit_rss', name='admin_news_edit_rss'),
    url(r'^news/edit/hand$', 'myapp.views.admin_news_edit_hand', name='admin_news_edit_hand'),
    url(r'^insert/hand$', "myapp.views.insert_news_hand", name='insert_news_hand'),
    url(r'^delete/rss$', "myapp.views.delete_news_rss", name='delete_news'),
    url(r'^view/price$', "myapp.views.view_price", name='view_price'),
    url(r'^insert/price$', "myapp.views.insert_price", name='insert_price'),
    url(r'^delete/news$', 'myapp.views.delete_news_rss', name='delete_news_rss'),
    url(r'^delete/news1/([^/]+)/$', 'myapp.views.delete_news_rss1', name='delete_news_rss1'),
    #url(r'^insert/news$', 'myapp.feed.update_feeds', name='insert_news_rss'),
    url(r'^login$', 'myapp.views.login', name='login'),

    #url(r'^insert/hand$', '', name='insert_news_hand'),


)
