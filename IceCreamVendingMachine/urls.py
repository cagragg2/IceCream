from django.conf.urls import patterns, include, url

from IceCreamVendingMachine import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),

	#url(r'^(?P<iceCreamID>\d+)/$', views.detail, name='detail'),

	url(r'^index/$', views.login, name='login'),

	url(r'^successLogin/$', views.successLogin, name='successLogin'),
	url(r'^failureLogin/$', views.failureLogin, name='failureLogin'),
	url(r'^iceCreamList/$', views.iceCreamList, name='iceCreamList'),
	url(r'^(?P<iceCreamID>\d+)/storeList/$', views.storeList, name='storeList'),
	url(r'^(?P<storeID>\d+)/storeAvailableList/$',views.storeAvailableList, 			name='storeAvailableList'),
	url(r'^(?P<iceCreamID>\d+)/successBuy/$', views.successBuy, name='successBuy'),
	url(r'^failureBuy/$', views.failureBuy, name='failureBuy'),
	url(r'^(?P<iceCreamID>\d+)/receipt/$', views.receipt, name='receipt'),
	url(r'^main/$', views.main, name = 'main'),
	url(r'^stores/$', views.stores, name = 'stores'),
	url(r'^select/$', views.select, name = 'select'),
	url(r'^warning/$', views.warning, name = 'warning')
)
