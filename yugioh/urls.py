from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'cards.views.search', name='search'),
    
    #url(r'^card/$', 'cards.views.index', name='card'),
    url(r'^card/(\d+)$', 'cards.views.single_card', name='single_card'),
    
    url(r'^booster/(\d+)$', 'cardsources.views.view_booster', name='booster'),

    url(r'^admin/', include(admin.site.urls)),
)
