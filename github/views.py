from django.views.generic.base import TemplateView

from github.api import Api
from githubapi import settings


class IndexView(TemplateView):
    template_name = "api/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        api = Api()
        user = api.get_user(getattr(settings, "GITHUB_USERNAME", ""))
        context["github_user"] = user
        context["blog"] = {
            "name": getattr(settings, "USER_BLOG_NAME", ""), "url": getattr(settings, "USER_BLOG_URL", "")
        }
        return context
