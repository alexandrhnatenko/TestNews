from django.conf.urls import url
from django.contrib import admin

from news.views import (PostListApiView, PostApiView, CommentListApiView,
                        CommentApiView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/$', PostListApiView.as_view(), name='posts_list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostApiView.as_view(), name='post'),
    url(r'^posts/(?P<post_id>[0-9]+)/comments/$', CommentListApiView.as_view(),
        name='comments_list'),
    url(r'^posts/(?P<post_id>[0-9]+)/comments/(?P<pk>[0-9]+)/$',
        CommentApiView.as_view(), name='comment'),
]
