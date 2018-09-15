from django.conf.urls import url
from forum import views
from forum.views import ForumView

app_name="forum"

urlpatterns=[
	url(r'^$',ForumView.as_view(),name='forum'),
	url(r'status/$',views.Status,name='status'),
	#url(r'status/(?P<pk>\d+)/update/$',views.updateStatus,name='update_stat_with_pk'),
	# url(r'^status/(?P)<slug>[-\w]+)/edit/$',views.edit_stat,name='edit_stat'),

]
