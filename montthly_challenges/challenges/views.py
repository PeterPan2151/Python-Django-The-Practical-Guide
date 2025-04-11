from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': 'Buy a car',
    'february': 'Rent a new home',
    'march': 'Get in the gym', 
    'april': 'finish Django Course',
    'may': 'Finish databases course',
    'june': 'Apply for jobs',
    'july': 'Keep leraning',
    'august': 'Buy a new laptop',
    'september': 'save money',
    'octuber': 'save more money',
    'november': 'keep saving money',
    'december': None
}

# Create your views here.
def home(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid Month')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month
        })
    except:
        return HttpResponseNotFound('<h1>Thihh  s month is not supported</h1>')
    

