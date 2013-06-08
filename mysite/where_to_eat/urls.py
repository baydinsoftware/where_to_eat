from django.conf.urls import patterns, url

from where_to_eat import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^create_ballot/$', views.create_ballot, name='create_ballot'),
    url(r'^create_ballot_submit/$', views.create_ballot_submit, name='create_ballot_submit'),

    url(r'^delete_confirmation/(?P<ballot_id>\d+)/$', views.delete_confirmation,
        name='delete_confirmation'),
    url(r'^delete_ballot/(?P<ballot_id>\d+)/$', views.delete_ballot, name='delete_ballot'),
        
    url(r'^(?P<ballot_id>\d+)/$', views.ballot, name='ballot'),
    url(r'^(?P<ballot_id>\d+)/sign_in/$', views.sign_in, name='sign_in'),
    url(r'^(?P<ballot_id>\d+)/add_option/$', views.add_ballot_option, name='add_ballot_option'),
    url(r'^(?P<ballot_id>\d+)/get_options/$', views.get_ballot_options, name='get_ballot_options'),
    url(r'^(?P<ballot_id>\d+)/submit_ballot/$', views.submit_ballot, name='submit_ballot'),
    url(r'^(?P<ballot_id>\d+)/results/$', views.results, name='results'),
    
)
