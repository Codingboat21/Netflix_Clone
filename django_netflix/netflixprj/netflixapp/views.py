from django.shortcuts import render, HttpResponse ,redirect
from django.contrib.auth import authenticate
from .models import CustomUser,Profile, Movie
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("profile")
    return render(request,'index.html')

def Login(request):
    if request.method=="POST":
        name=request.POST.get('login')
        pas=request.POST.get('password')
        user=authenticate(request,username=name,password=pas)
        
        if user is None:
            return HttpResponse(" not valid !!....")

        else:
            return redirect('home')



    return render(request,'account/login.html')

def Signup(request):
    if request.method=="POST":
        name=request.POST.get('username')
        email=request.POST.get("email")
        pas1=request.POST.get("password1")
        pas2=request.POST.get("password2")

        

        if pas1 ==pas2:
            user=CustomUser.objects.create_user(username=name, email=email, password=pas1)

            user.save()
            return redirect('login')
        
        else:
            return HttpResponse("Your Password did not match !!...")



    return render(request,'account/signup.html')


@login_required(login_url="login")
def profiles(request):
    profiles=request.user.profiles.all()
    
    context={
        'profiles':profiles
    }
    return render (request,'profilelist.html',context)

def profileCreate(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age_limit=request.POST.get('age_limit')
        # print(name,age_limit)

        new_profile = Profile(name=name,age_limit=age_limit)

        user1= request.user.profiles.create(name=name,age_limit=age_limit)

        new_profile.save()
        # print('profile created')
        user1.save()
        # print("user profile create")
        return redirect ('profile')

    return render(request,'profilecreate.html')



@login_required(login_url='profile')
def movielist(request,profile_id):
    profile=Profile.objects.get(uuid=profile_id)
    movies=Movie.objects.filter(age_limit=profile.age_limit)
    if profile not in request.user.profiles.all():
        return redirect('profile')


    return render(request,'movielist.html',{'movies':movies})

def movieDetail(request,movie_id):
    movies=Movie.objects.get(uuid=movie_id)

    return render(request,'moviedetail.html',{'movie':movies})



def PlayMovie(request,movie_id):
    movies=Movie.objects.get(uuid=movie_id)

    video=movies.videos.values()
    return render(request,'playmovie.html',{'movie':list(video)})