
from django.shortcuts import render
from mywatchlist.models import Mywatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):
    data_watchlist = Mywatchlist.objects.all()
    context = {
    'nama': 'Aulia Satrio Wijoyo',
    'npm' : '2106752123',
    'list_mywatchlist' : data_watchlist
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    data_watchlist = Mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_json_by_id(request, id):
    data_watchlist = Mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")

def show_xml(request):
    data_watchlist = Mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_xml_by_id(request, id):
    data_watchlist = Mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")