#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : urls.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 23.09.2017
# Last Modified Date: 23.09.2017
# Last Modified By  : Channith Am <amcnith@gmail.com>

# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
        url(r'^$', views.HomePageView.as_view()),
        url(r'^about/$', views.AboutPageView.as_view()),  # Add this /about/ route

]
