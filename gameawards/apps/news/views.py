from django.shortcuts import render_to_response, get_object_or_404
from news.models import Newspost
from django.template import RequestContext
from content.models import Slide
from runs.models import Game, Run

def index(request):
    r = get_object_or_404(Run, current_run=True)

    home_slide_list = Slide.objects.filter(belongs_to = 1).order_by('title')
    event_slide_list = Slide.objects.filter(belongs_to = 2).order_by('title')
    getstarted_slide_list = Slide.objects.filter(belongs_to = 3).order_by('title')
    games_slide_list = Slide.objects.filter(belongs_to = 4).order_by('title')
    contact_slide_list = Slide.objects.filter(belongs_to = 5).order_by('title')
    game_list = Game.objects.filter(run=r).order_by('-added_date')[:3]
    news = Newspost.objects.all().order_by('-pub_date')[:3]
    
    return render_to_response(
        'news/index.html',
        {
            'news':news,
            'home_slide_list': home_slide_list,
            'event_slide_list': event_slide_list,
            'getstarted_slide_list': getstarted_slide_list,
            'games_slide_list': games_slide_list,
            'contact_slide_list': contact_slide_list,
            'game_list': game_list,
        },
        context_instance=RequestContext(request))



def detail(request, newspost_id):
    p = get_object_or_404(Newspost, pk=newspost_id)
    return render_to_response(
        'news/detail.html', 
        {'post': p}, 
        context_instance=RequestContext(request))
