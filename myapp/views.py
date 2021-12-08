from django.http import HttpResponse
from django.shortcuts import render
from django.template import context, Context


def index(request):
    contextvalue = {"valeur": "valeurTest", "table": [1, 2, 3, 4, 5]}
    # context.Context.push(test)
    return render(request, 'index.html', contextvalue)
    # return HttpResponse("<h1>Bienvenue sur Django - INDEX !</h1>")


# Create your views here.
def hello(request):
    text = "<h1>Bienvenue sur Django - HELLO !</h1><p>Ceci est une vue</p>"
    return HttpResponse(text)


def result(request, number):
    text = "<p>Le résultat de la reqûete est %d</p>" % number
    textAlt = "<p>Le résultat de la reqûete est %d</p>" % number

    return HttpResponse(text) if number > 18 else HttpResponse(f"<h1>Bienvenue sur Django - result !</h1>{textAlt}")
