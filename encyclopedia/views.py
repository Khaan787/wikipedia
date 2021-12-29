from django.http.response import HttpResponse
from django.shortcuts import render
from django import forms

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
        if search_query not in entries:
            # the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were 'ytho', then 'Python' should appear in the search results.
            for i in search_query:
                if search_query in i:
                    return render(request, "encyclopedia/search.html", {
                        "search": i                        
                    })
                
                else:
                    return HttpResponse("Entry not Found")    
           
        else:   
            return render(request,"encyclopedia/search.html", {
                "search": util.get_entry(search_query)
            })




                



    