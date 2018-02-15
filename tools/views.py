# -*- coding: utf-8 -*-
# _____           _
#|_   _|         | |
#  | | ___   ___ | |___  _____
#  | |/ _ \ / _ \| / __||_   _|
#  | | (_) | (_) | \__ \  | |
#  \_/\___/ \___/|_|___/- |_| ...
#        ~ code by Alr ~
#
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from django.shortcuts import redirect
import nmap
from speedtest import *
import commands
import socket
from bs4 import BeautifulSoup
import requests
import re
import urllib
from geoip import geolite2
# Create your views here.


# Clase template info
class tools(TemplateView):
    template_name= "template.info.html"

# Funcion que permite resolver peticiones
def tactools(request):
    if request.method == 'GET':
        user = os.getlogin()
        OS = os.name
        sys = os.uname()
        date = datetime.datetime.today()
        results = commands.getoutput('speedtest-cli --simple')
        try:
            url = "www.showmyip.gr"
            r  = requests.get("http://" +url)
            data = r.text
            soup = BeautifulSoup(data, 'html.parser')
            span = soup.find("span", class_="ip_address")
            ip = span.text
            return render(request, 'template.tools.html', {'date': date, 'user': user, 'results': results })
        except:
            return render(request, 'template.Error.html')
    else:
        return render(request, 'template.Error.html')

def info(request):
    pass

def usuario(request):
    pass

def direccion(request):
    pass

def tetsvelocidad(request):
    pass
