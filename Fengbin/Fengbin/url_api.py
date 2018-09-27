from django.conf.urls import url
from view_api import *

urlpatterns = [
    url(r'^website/$', WebsiteAllList.as_view()),
]