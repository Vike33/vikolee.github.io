from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html',  ) 
def counter(request):
    words = request.POST['text']
    amount_of_words = len(words.split())
    amount_of_letters = len(words)
    wors = 'The amount of letters is '
    if amount_of_words <= 4:
        return render(request, 'counter.html', {'amount': amount_of_words})
    else:
        return render(request, 'counter.html',{'amounts': amount_of_letters, 'wor': wors} )