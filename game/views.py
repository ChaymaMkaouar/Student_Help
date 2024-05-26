from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('game/index.html')
    return HttpResponse(template.render(request=request))

def aurevoir(request):
    template = loader.get_template('game/aurevoir.html')
    return HttpResponse(template.render(request=request))

