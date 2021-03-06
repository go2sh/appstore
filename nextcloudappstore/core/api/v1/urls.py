from django.conf.urls import url
from django.views.decorators.http import etag
from nextcloudappstore.core.api.v1.views import AppView, AppReleaseView, \
    CategoryView, app_api_etag, category_api_etag

urlpatterns = [
    url(r'^platform/(?P<version>\d+\.\d+\.\d+)/apps\.json$',
        etag(app_api_etag)(AppView.as_view()), name='app'),
    url(r'^apps/releases/?$', AppReleaseView.as_view(),
        name='app-release-create'),
    url(r'^apps/(?P<pk>[a-z_]+)/?$', AppView.as_view(), name='app-delete'),
    url(r'^apps/(?P<app>[a-z_]+)/releases/(?P<version>\d+\.\d+\.\d+'
        r'(?:-nightly)?)/?$',
        AppReleaseView.as_view(), name='app-release-delete'),
    url(r'^categories.json$',
        etag(category_api_etag)(CategoryView.as_view()), name='category'),
]
