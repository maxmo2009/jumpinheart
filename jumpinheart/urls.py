from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jumpinheart.views.home', name='home'),
    # url(r'^jumpinheart/', include('jumpinheart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^signup$', 'auth.views.signup'),
	url(r'^signup-form$', 'auth.views.signup_form'),
	url(r'^$', 'stories.views.index'),
	url(r'^logout$', 'auth.views.logout_view'),
	url(r'^login$', 'auth.views.login_view'),
	url(r'^login-form$', 'auth.views.login_form'),
	url(r'^check-username$', 'auth.views.check_username'),
	url(r'^check-email$', 'auth.views.check_email'),
    # url(r'^admin/', include(admin.site.urls)),
)
