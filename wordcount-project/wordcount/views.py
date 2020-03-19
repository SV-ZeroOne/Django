from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse("Hello World")
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    # prints to the terminal
    #print(fulltext)
    wordlist = fulltext.split()
    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # Add to the dictionary
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sorted_words':sorted_words})


def about(request):
    return render(request, 'about.html')