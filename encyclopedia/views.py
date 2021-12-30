from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms
import re

from . import util
import encyclopedia

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, url):
    return render(request, "encyclopedia/titlepage.html",{
        "page": util.get_entry(url)
    })

def search(request):
  
        search_query = request.GET['q']
        
        entries = util.list_entries()

    # If the query does not match the name of an encyclopedia entry
        if search_query in entries:
            # the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were 'ytho', then 'Python' should appear in the search results.
            
                
            return render(request, "encyclopedia/search.html", {
                "search":  util.get_entry(search_query)
                })
                                
        else:
            matches = [item for item in entries if search_query.casefold() in item]
            print(entries)
            print(matches)
            return render(request, "encyclopedia/search.html", {
                "search":  util.get_entry(search_query)
            }) ### FIX THIS ACCORDINGLY
            






                



    
