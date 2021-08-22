from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'homepage.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    
    worddic = {}

    for word in wordlist:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    
    sortlist = sorted(worddic.items(), key = operator.itemgetter(1), reverse= True)
    
    return render(request, 'counted.html', {'fulltext': fulltext, 'count': len(wordlist), 'worddic': sortlist})

def about(request):
    return render(request, 'aboutme.html')