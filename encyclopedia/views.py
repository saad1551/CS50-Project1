from django.shortcuts import render
from markdown import markdown
from django.urls import reverse

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
        "content": markdown(util.get_entry(title))
    })