from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    'january': 'Learn Django',
    'febraury': 'Cherish my loved ones',
    'march': 'Celebrate my birthday',
    'april': 'Learn LINUX',
    'may': 'Celebrate Mothers day',
    'june': 'Learn GIT',
    'july': 'Learn Java',
    'august': 'Watch Peace Maker season 2',
    'september': 'Celebrate independence',
    'octuber': 'Suit up for halloween',
    'november': 'Meditate the whole month',
    'december': None
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month - 1]
    redirect_url = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month': month
        })
    except:
        raise Http404()
    

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })
    
