from django.conf.urls import url
from api.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
]