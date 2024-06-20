from django.shortcuts import render
from django.http import HttpResponseRedirect

from webapp.cat_db import CatDb


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        CatDb.name = request.POST.get('name')
        return HttpResponseRedirect('/cat_stats')


def cat(request):
    if request.method == "GET":
        CatDb.set_state()
        context = {
            'name': CatDb.name,
            'age': CatDb.age,
            'fullness': CatDb.fullness,
            'happiness': CatDb.happiness,
            'state': CatDb.current_state
        }
        return render(request, 'cat_stats.html', context=context)
    else:
        if request.POST.get('action') == 'play':
            CatDb.play()
        elif request.POST.get('action') == 'feed':
            CatDb.feed()
        else:
            CatDb.sleep()

        return HttpResponseRedirect('/cat_stats')

