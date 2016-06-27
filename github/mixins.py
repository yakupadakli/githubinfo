from django.core.cache import cache

from github.api import Api
from githubapi import settings


class GithubMixin(object):
    github_user = None

    def get_context_data(self, **kwargs):
        context = super(GithubMixin, self).get_context_data(**kwargs)
        self.get_github_user()
        context["github_user"] = self.github_user
        return context

    def get_github_user(self):
        github_user = cache.get("github_user")
        if not github_user:
            api = Api()
            github_user = api.get_user(getattr(settings, "GITHUB_USERNAME", ""))
            cache.set("github_user", github_user)
        self.github_user = github_user
        return self.github_user
