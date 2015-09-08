from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'cards.views.index', name='index'),
    
    url(r'^search/$', 'cards.views.search', name='search'),
    
    #url(r'^card/$', 'cards.views.index', name='card'),
    url(r'^card/(?P<card_id>\d+)/$', 'cards.views.single_card', name='single_card'),
    
    url(r'^booster/(?P<booster_id>\d+)/$', 'cardsources.views.view_booster', name='booster'),
    url(r'^deck/(?P<deck_id>\d+)/$', 'cardsources.views.view_deck', name='deck'),

    url(r'^admin/', include(admin.site.urls)),
)
