from django.core.cache import cache
from django.views.generic.base import TemplateView

from github.api import Api
from github.mixins import GithubMixin
from githubapi import settings


class IndexView(GithubMixin, TemplateView):
    template_name = "github/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["blog"] = {
            "name": getattr(settings, "USER_BLOG_NAME", ""), "url": getattr(settings, "USER_BLOG_URL", "")
        }
        return context


class RepoListView(GithubMixin, TemplateView):
    template_name = "github/repo_list.html"

    def get_context_data(self, **kwargs):
        context = super(RepoListView, self).get_context_data(**kwargs)
        repo_list = cache.get("repo_list")
        if not repo_list:
            api = Api()
            repo_list = api.get_user_repos(getattr(settings, "GITHUB_USERNAME", ""))
            cache.set("repo_list", repo_list)
        context["repo_list"] = repo_list
        return context


class FollowerListView(GithubMixin, TemplateView):
    template_name = "github/follower_list.html"

    def get_context_data(self, **kwargs):
        context = super(FollowerListView, self).get_context_data(**kwargs)
        follower_list = cache.get("follower_list")
        if not follower_list:
            api = Api()
            user_list = []
            follower_list = api.get_user_followers(getattr(settings, "GITHUB_USERNAME", ""))
            for follower in follower_list:
                user = api.get_user(follower.get("login"))
                user_list.append(user)
            cache.set("follower_list", user_list)
        context["follower_list"] = follower_list
        return context
