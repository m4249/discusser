from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
# for flash messages
from django.contrib import messages
# for sessions of login authenticate and logout
from django.contrib.auth import authenticate,login,logout
# for restricted pages what user and non user can see
from django.contrib.auth.decorators import login_required
from .models import Room, Topic
from .forms import RoomForm
# Create your views here.
# rooms = [
#     {'id':1,'name':'sam'},
#     {'id':2,'name':'bam'}
#     ]

# books = [{id:1,'name':'sherlock'}]

# dont use login()as it is built in funcn
def loginPage(request):
#if user is in session if u go to /login it will take you to home
# it will not prompt to login again if u go to /login
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            # adding session in database and browser so user can login
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Username or password is incorrect')
    context={}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # gets all the users of the room
    rooms = Room.objects.filter(
     Q(topic__name__icontains = q)|
     Q(name__icontains=q)|Q(description__icontains=q))

    topic = Topic.objects.all()
    # counts room to display in home.html
    room_count = rooms.count()   

    context = {'rooms':rooms,'topics':topic,'room_count':room_count}
    return render(request,'base/home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)

# prompt them to login
@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'base/room_form.html',context)

@login_required(login_url='/login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)
#  if user is host then only let him edit
    if request.user != room.host:
        return HttpResponse('you are not allowed')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}

    return render(request, 'base/room_form.html',context)

@login_required(login_url='/login')  
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    #  if user is host then only let him delete
    if request.user != room.host:
        return HttpResponse('you are not allowed')
    if request.method =='POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html',{'obj':room})

 