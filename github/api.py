import requests


class Api(object):

    def __init__(self):
        self._host = "api.github.com/"
        self._user_url = "users/%s"
        self._user_repos_url = "users/%s/repos"
        self._user_followers_url = "users/%s/followers"
        self._user_following_url = "users/%s/following"

    def _build_url(self, target):
        return "https://%s%s" % (self._host, target)

    def _get(self, url, params=None, **kwargs):
        url = self._build_url(url)
        response = requests.get(url, params=params, **kwargs)
        if response.ok:
            return response.json()
        return None

    def get_user(self, username):
        user_url = self._user_url % username
        user_data = self._get(user_url)
        return user_data

    def get_user_repos(self, username):
        repos_url = self._user_repos_url % username
        repos_data = self._get(repos_url)
        return repos_data

    def get_user_followers(self, username):
        followers_url = self._user_followers_url % username
        followers_data = self._get(followers_url)
        return followers_data

    def get_user_following(self, username):
        following_url = self._user_following_url % username
        following_data = self._get(following_url)
        return following_data
