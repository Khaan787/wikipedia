from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django import forms
from django.urls import reverse
import random
import markdown2
from . import util
import encyclopedia


md = markdown2.Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    
    that_entry = entry
 
    return render(request, "encyclopedia/titlepage.html",{
        "page": md.convert(util.get_entry(entry)),
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
                "search": md.convert(util.get_entry(search_query))
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
             
             return HttpResponseRedirect(reverse("entry", args=(title,)))
             

    else:
        return render(request,"encyclopedia/create_page.html")
    

def edit_page(request,that_entry):

        
        if request.method == "POST":
            content_page = request.POST['textarea']

            util.save_entry(that_entry, content_page)
            
            return HttpResponseRedirect(reverse("entry", args=(that_entry,)))
            

        else:
            return render(request,"encyclopedia/edit_page.html",{
                "that_page_title": that_entry,
                "that_page_content": md.convert(util.get_entry(that_entry))
            })
            

def random_page(request):
    the_random_page = random.choice(util.list_entries())

    return render(request,"encyclopedia/random_page.html",{
        "random_page": md.convert(util.get_entry(the_random_page))
    })
        
    

        



                



    