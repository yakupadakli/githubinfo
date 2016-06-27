from django.conf.urls import url

from github.views import IndexView, RepoListView, FollowerListView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^repos/$', RepoListView.as_view(), name="repos"),
    url(r'^followers/$', FollowerListView.as_view(), name="followers"),
]
