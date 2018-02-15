#!/usr/bin/env python
# coding: utf-8
# _____           _
#|_   _|         | |
#  | | ___   ___ | |___  _____
#  | |/ _ \ / _ \| / __||_   _|
#  | | (_) | (_) | \__ \  | |
#  \_/\___/ \___/|_|___/- |_| ...
#        ~ code by Alr ~
#
from django.conf.urls import url
from .views import tools, tactools

# Urls App Tools
urlpatterns = [
    url(r'^tools', tools.as_view(), name= 'tools'),
    url(r'^tactools', tactools, name= 'tactools'),
]
