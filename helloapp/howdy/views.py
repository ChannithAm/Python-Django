#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : views.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 23.09.2017
# Last Modified Date: 23.09.2017
# Last Modified By  : Channith Am <amcnith@gmail.com>
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"
