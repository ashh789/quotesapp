from django.shortcuts import render,get_object_or_404
from . models import Tag,Person,Quote

def tagpage(request):
    tag_list=Tag.objects.all()
    return render(request,"quotesapp/taglist.html",{"tag_list":tag_list})

def quotepage(request,slug):
    tag=get_object_or_404(Tag,slug=slug)
    return render(request,"quotesapp/quotepage.html",{"tag":tag})

def personpage(request):
    person=Person.objects.all()
    return render(request,"quotesapp/personpage.html",{"person":person})

def check(request):
    return render(request,"quotesapp/check.html")

def personquotes(request,slug):
    person=get_object_or_404(Person,slug=slug)
    person_quotes=person.quote_set.all()
    return render(request,"quotesapp/personquotespage.html",{"person_quotes":person_quotes})
