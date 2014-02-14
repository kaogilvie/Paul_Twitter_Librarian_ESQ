from django.conf.urls import patterns, url
import views

urlpatterns = patterns ('', 
	# ex: /paul/
	url(r'^$', views.index, name='index')
	)