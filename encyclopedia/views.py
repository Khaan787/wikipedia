from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, url):
    return render(request, "encyclopedia/titlepage.html",{
        "page": util.get_entry(url)
    })

def search(request):
    # if the search query is equal to any of entries in the list "entries"
        search_query = request.GET

        if search_query == util.list_entries():

            # user should be redirected to that entry’s page
            return render(request,"encyclopedia/search.html", {
                "search_query": util.get_entry()
            })

    # if not
        # Print "Not Found"