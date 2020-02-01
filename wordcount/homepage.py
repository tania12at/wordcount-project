from django.shortcuts import render
import operator

def home(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    worddict = {}
    for item in wordlist:
        if item in worddict:
            worddict[item]+=1
        else:
            worddict[item] = 1
    sorted_dict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {"fulltext":fulltext, "count":len(wordlist), "itemdict":sorted_dict})


def about(request):
    return render(request, "about.html")
