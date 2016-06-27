from django.conf.urls import url

from github.views import IndexView, RepoListView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^repos/$', RepoListView.as_view(), name="repos"),
]
