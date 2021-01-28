from django.shortcuts import render,redirect
from movieupdate.models import Movie
from django.http import HttpResponse
from django.template.context_processors import csrf 

# Create your views here.
"""def update(request, moviename):
#    u_movie = Movie.objects.get(pk = moviename)
 ##   #you can do this for as many fields as you like
   ### #here I asume you had a form with input like <input type="text" name="name"/>
    #s###o it's basically like that for all form fields
    u_movie.moviename = request.POST.get('moviename')
    u_movie.save()
    return HttpResponse('updated')
"""
def add_view(request):
    if request.method == 'POST':
        u_movie = request.POST.get('moviename','')
        if(request.FILES.get('movieimg','')):
            u_img=request.FILES['movieimg']
            m=Movie(moviename=u_movie)
            m.movieimg=u_img
            m.save()
            done="ADDED SUCCESSFULLY!!!"
            return render(request,'addmovie.html/',{'done':done}) 
    c={}
    c.update(csrf(request))
    return render(request,'addmovie.html',c)

def homesuper_view(request):
    if request.user.is_authenticated:
        movies=Movie.objects.all()
        for m in movies:
            if m.movieimg:
                print(m.movieimg.path) 
        return render(request,'homesuper.html',{'movies':movies})
    else:
        return redirect('/accounts/login/')


def delete_view(request):
    u_movie=request.POST.get('movie_name','')
    m = Movie.objects.get(moviename = u_movie)
    m.delete()
    return render(request,'homesuper.html')
