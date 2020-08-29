from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import GuessNumber
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumber.objects.all()    
#    return HttpResponse('<h1>Hello, Inflearn!</h1>')
    return render(request, "lotto/default.html", {"lottos" : lottos})

def post(request):
    if request.method == "POST":
        # save data
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index')
            
    else:
        form = PostForm()
        return render(request, "lotto/form.html", {"form" : form})

def detail(request, lottokey):
    lotto = GuessNumber.objects.get(pk = lottokey)
    print(lotto)
    return render(request, "lotto/detail.html", {"lotto" : lotto})