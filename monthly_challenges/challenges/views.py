from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse;

# Create your views here.
challenges = {
    "january": "Jan",
    "february": "feb",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "aug",
    "september": "sep",
    "octuber": "oct",
    "november": "Nov",
    "december": None
}

def index(request) :
    months = list(challenges.keys())
    return render(request, 'challenges/index.html', {'months': months})

def monthly_challenge_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid Month')
    forward_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'titles': month,
            })
    except:
        raise Http404()
    

