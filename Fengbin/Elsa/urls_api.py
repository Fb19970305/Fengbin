from django.conf.urls import url
from views_api import *

urlpatterns = [
    url(r'^allcloth/', ElsaAllList.as_view()),
]