import requests


class Api(object):

    def __init__(self):
        self._host = "api.github.com/"
        self.user_url = "users/%s"

    def _build_url(self, target):
        return "https://%s%s" % (self._host, target)

    def _get(self, url, params=None, **kwargs):
        url = self._build_url(url)
        response = requests.get(url, params=params, **kwargs)
        if response.ok:
            return response.json()
        return None

    def get_user(self, username):
        user_url = self.user_url % username
        user_data = self._get(user_url)
        return user_data
