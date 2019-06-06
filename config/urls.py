from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.conf.urls import url

from alwahaj.core.views import contactUs,overview,index,adminSetting

urlpatterns = [

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path('users/', include('alwahaj.users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here
    url(r'^$', index.homeView, name='home'),
    url(r'^logout/$', index.logoutUser, name='logout'),
    url(r'^projects/', include('core.urls.projects')),
    url(r'^solutions/', include('core.urls.solutions')),
    url(r'^staff/', include('core.urls.staff')),
    url(r'^addCompany/$', adminSetting.addCompany, name='addCompany'),
    url(r'^addSystem/$', adminSetting.addSystem, name='addSystem'),
    url(r'^addProject/$', adminSetting.addProject, name='addProject'),
    url(r'^linkSystem/$', adminSetting.linkSystem, name='linkSystem'),
    url(r'^linkStaff/$', adminSetting.linkStaff, name='linkStaff'),
    url(r'^addStaff/$', adminSetting.addStaff, name='addStaff'),
    url(r'^contactUs/$', contactUs.contactUs, name='contactUs'),
    url(r'^overview/$', overview.overviewView, name='overview'),
    url(r'^delete/$', adminSetting.delete, name='delete'),
    url(r'^update/$', adminSetting.update, name='update'),
    # url(r'^update/(?P<key>\w{0,50})/$', adminSetting.update),
    url(r'^update/(?P<key>[0-9]+)/$', adminSetting.update),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            '400/',
            default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')},
        ),
        path(
            '403/',
            default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')},
        ),
        path(
            '404/',
            default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')},
        ),
        path('500/', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
