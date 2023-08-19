from django.shortcuts import render, redirect
from markdown import markdown
from django.urls import reverse
from .forms import MyForm, NewPageForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from . import util


def index(request):
    headings = util.list_entries()
    links = []
    entries = []
    for heading in headings:
        links.append(reverse("entry", kwargs={"title": heading.lower()}))
    for i in range(len(headings)):
        entries.append({
            "heading":headings[i],
            "link": links[i]
        })
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize(),
        "content": markdown(util.get_entry(title)) if util.get_entry(title) else "<h1>Sorry! The page you requested doesn't exist</h1>"
    })

@require_POST
def search(request):
    form = MyForm(request.POST)
    if form.is_valid():
        search_string = form.cleaned_data['q']
        titles = util.list_entries()
        matchingTitles = []
        for title in titles:
            if search_string.lower() == title.lower():
                return redirect(reverse("entry", kwargs={"title": title.lower()}))
            elif title.lower().find(search_string.lower()) != -1:
                    matchingTitles.append(title)
        matchingEntries = []
        matchingLinks = []
        for matchingTitle in matchingTitles:
            matchingLinks.append(reverse("entry", kwargs={"title": matchingTitle.lower()}))
        for i in range(len(matchingTitles)):
            matchingEntries.append({
                "heading": matchingTitles[i],
                "link": matchingLinks[i]
            })
        if len(matchingEntries) != 0:
            return render(request, "encyclopedia/index.html", {
                "entries": matchingEntries
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "<h3>No matching entries found</h3>"
            })


def new(request):
    form = NewPageForm()
    return render(request, "encyclopedia/newpage.html", {
        "form":form
    })