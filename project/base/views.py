from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
# for flash messages
from django.contrib import messages
# for sessions of login authenticate and logout
from django.contrib.auth import authenticate,login,logout
# for restricted pages what user and non user can see
from django.contrib.auth.decorators import login_required
from .models import Room, Topic ,Message, User
# used for register page

from .forms import RoomForm,UserForm,MyUserCreationForm
# Create your views here.
# rooms = [
#     {'id':1,'name':'sam'},
#     {'id':2,'name':'bam'}
#     ]

# books = [{id:1,'name':'sherlock'}]

# dont use login()as it is built in funcn
def loginPage(request):
    page = 'login'
#if user is in session if u go to /login it will take you to home
# it will not prompt to login again if u go to /login
    if request.user.is_authenticated:
        return redirect('/')
 
    if request.method == 'POST':
        username = request.POST.get('username').lower()
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
    context={'page':page}
    return render(request,'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            # if form valid user get created
            user = form.save(commit=False)
            user.username  = user.username.lower()
            user.save()
            # when registerd login function push them into session
            login(request, user)
            return redirect('/')
        else:
            messages.error(request,'Cant get you in')

    context={'form':form}
    return render(request,'base/login_register.html',context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # gets all the users of the room
    rooms = Room.objects.filter(
     Q(topic__name__icontains = q)|
     Q(name__icontains=q)|Q(description__icontains=q))

    topic = Topic.objects.all()[0:5]
    # counts room to display in home.html
    room_count = rooms.count()   
# this is for specific if we go to web development in recent activity 
# only recent javascript activity will show
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {'rooms':rooms,'topics':topic,'room_count':room_count,'room_messages':room_messages}
    return render(request,'base/home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    # give the set of messages that are related to this specific room
    roomMessages = room.message_set.all()

    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
           user = request.user,
           room=room,
           body=request.POST.get('body') 
        )
        room.participants.add(request.user)
        # for fully reload
        return redirect('room',pk=room.id)
    context = {'room':room,'roomMessages':roomMessages,'participants':participants}
    return render(request,'base/room.html',context)


def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user':user,'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'base/profile.html',context)





# prompt them to login
@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic , created = Topic.objects.get_or_create(name = topic_name)
        
        Room.objects.create(
            host=request.user,
            topic = topic,
            name= request.POST.get('name'),
            description = request.POST.get('description'),
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     # as we are not selecting host 
        #     # so default host will be the one logged in
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        return redirect('home')

    context={'form':form,'topics':topics}
    return render(request, 'base/room_form.html',context)

@login_required(login_url='/login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)
    topics = Topic.objects.all()

#  if user is host then only let him edit
    if request.user != room.host:
        return HttpResponse('you are not allowed')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic , created = Topic.objects.get_or_create(name = topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form':form,'topics':topics,'room':room}

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

 
 
@login_required(login_url='/login')  
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    #  if user is host then only let him delete
    if request.user != message.user:
        return HttpResponse('you are not allowed')

    if request.method =='POST':
        message.delete()
        return redirect('/')
    return render(request, 'base/delete.html',{'obj':message})

@login_required(login_url = '/login')
def updateUser(request):
    user = request.user
    form = UserForm(instance = user)

    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance = user)
        if form.is_valid():
            form.save()
            return redirect('user-profile',pk = user.id)

    context={'form':form}
    return render(request,'base/update-user.html',context)


def topicUser(request):
    topics= Topic.objects.filter()
    context={'topics':topics}
    return render(request,'base/topics.html',context)

