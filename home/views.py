from http.client import responses
from django.shortcuts import render
from os import listdir
from os.path import isfile, join
from .models import Movie
from django.apps import apps

# Create your views here.
def error(request):
    return render(request, 'pages/error.html')
def index(request):
    path = "C:/Users/NHATMINH/Desktop/Projects/Django/Titanus/home/"
    if request.user.is_authenticated:
        account_path = "/account/profile/"
    else:
        account_path = "/account/login/"
    context = {
        "poster":{},
        "hotmovies":{},
        "movies": Movie.objects.all(),
        "auth":account_path
        }
    if request.user.is_authenticated:
        context["avatar"] = str(apps.get_model("useraccount", "UserProfile").objects.get(user=request.user).avatar)
    else:
        context["avatar"] = "0"
    files1 = listdir(path+"static/poster/horizontal")
    for f in files1:
        if isfile(join(path+"static/poster/horizontal", f)):
            context["poster"][files1.index(f)] = "/poster/horizontal/" + f
    files2 = listdir(path+"static/poster/vertical")
    for f in files2:
        if isfile(join(path+"static/poster/vertical", f)):
            context["hotmovies"][files2.index(f)] = "/poster/vertical/" + f
    return render(request, "pages/homepage.html",context)

def preview(request, mid):
    try:
        obj = Movie.objects.get(mid = mid)
    except:
        return error(request)

    m = obj.description.index(".") + 1
    context = {
        "title":obj.title,
        "thumbnail":obj.thumbnail,
        "description":[obj.description[:m],obj.description[m:]],
    }
    return render(request, "pages/preview.html", context)

def player(request, mid):
    try:
        obj = Movie.objects.get(mid = mid)
    except:
        return error(request)

    choices = []
    
    for i in range(7):
        obj = Movie.objects.order_by("?").first()
        m = obj.title.index(":")
        choices.append([
                obj.mid,
                obj.thumbnail,
                obj.title[:m],
                obj.title[m+1:]
            ])

    context = {
        "id":mid,
        "title":obj.title,
        "thumbnail":obj.thumbnail,
        "recommender":choices,
        "chapters":[]
    }
    print(choices)
    return render(request, "pages/player.html", context)
    
