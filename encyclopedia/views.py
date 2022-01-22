from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django import forms
from django.urls import reverse

from . import util
import encyclopedia


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    that_entry = entry
    
    return render(request, "encyclopedia/titlepage.html",{
        "page": util.get_entry(entry),
        "that_entry": that_entry
    })
    
def search(request):
    
        search_query = request.GET['q']
        entries = util.list_entries()

    # If the query does not match the name of an encyclopedia entry
        if search_query not in entries:
            # the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were 'ytho', then 'Python' should appear in the search results.
            for i in entries:
                if search_query.lower() in i.lower():     
                    return render(request, "encyclopedia/search.html", {
                        "search": i                                           
                    })
                
            else:
                return HttpResponse("Entry not Found")    
           
        else:   
            return render(request,"encyclopedia/search.html", {
                "search": util.get_entry(search_query)
            })

def create_page(request):
    if request.method == "POST":
        
        entries_list = util.list_entries()
        title = request.POST['title']
        content = request.POST['textarea']

        if title in entries_list:
            return HttpResponse("Entry already exists")

        else:
             util.save_entry(title, content)
             
             return render(request,"encyclopedia/titlepage.html",{
                 "page": util.get_entry(title)
             })

    else:
        return render(request,"encyclopedia/create_page.html")
    

def edit_page(request,that_entry):
        that_page_title = that_entry
        content_page = util.get_entry(that_entry)

        if request.method == "POST":
            util.save_entry(that_page_title, content_page)
            
            return render(request,"encyclopedia/titlepage.html",{
                "page": util.get_entry(that_page_title)
            })

        else:
            return render(request,"encyclopedia/edit_page.html",{
                "that_page_title": that_page_title,
                "that_page_content": content_page
            })
            


        
    

        



                



    