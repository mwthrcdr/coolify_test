from django.shortcuts import render

# Create your views here.
# date_app/views.py
from django.http import HttpResponse
from datetime import datetime

def current_datetime(request):
    now = datetime.now()
    html = f"<html><body>Obecna data i godzina: {now}</body></html>"
    return HttpResponse(html)
