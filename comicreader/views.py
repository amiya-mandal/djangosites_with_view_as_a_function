from django.shortcuts import render,render_to_response,redirect
from .models import *
from .forms import *
from django.contrib import auth
from django.http import *
from django.contrib.auth.decorators import login_required
import sys

# Create your views here.

def home(request):
    if request.user.is_authenticated():
        return redirect('login_home')
    else:
        obj = comicDataBase.objects.all()
        return render(request, 'home.html', {'fullname': 'Guest', 'obj': obj})
#show the login page
def login(request):
    return render(request,'login.html')

def authenticates(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/login_home')
    else:
        return HttpResponseRedirect('/accounts/invalid')



def login_home(request):
    if request.user.is_authenticated():
        obj = comicDataBase.objects.all()
        return render(request,'home.html',{'fullname':request.user.username,'obj':obj})
    else:
        return redirect('home')

def invalid(request):
    k='invalid Username or Password'
    return render(request,'login.html',{'error':k})

def logoutaccount(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def uploaded(request):
    if request.user.is_authenticated():
        u=User.objects.get(username=request.user)
        udata=userDataBase.objects.get(user=u)
        cdata=comicDataBase.objects.all().filter(userdatabse=udata)
        return render(request, 'home2.html', {'fullname': request.user, 'obj': cdata})


#for the sucess page
def regSucsess(request,i):
    a=User.objects.get(id=i)
    return render(request,'registration_success.html',{'obj':a})

def upSuccess(request):
    return render(request,'up_sucess.html')

#to delete a record
def deleteRecord(request,i):
   if request.user.is_authenticated():
       dcomic = comicDataBase.objects.get(id=i)
       dcomic.delete()
       return redirect('uploaded')
   else:
       return HttpResponseRedirect('/login/')



#uploading a file
def upload(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            u = User.objects.get(username=request.user)
            udata = userDataBase.objects.get(user=u)
            print request.user
            upform = comicForm(request.POST, request.FILES)

            if upform.is_valid():
                up = comicDataBase(
                    title=upform.cleaned_data['title'],
                    author=upform.cleaned_data['author'],
                    fileup=upform.cleaned_data['fileup'],
                    userdatabse=udata
                )
                try:
                    up.save()
                except:
                    print 'error', sys.exc_info()[0]
                    print sys.exc_info()[1]
                    return HttpResponseRedirect('/')

                return redirect('success2')

        return render(request, 'upload.html', {'form': comicForm()})
    else:
        return HttpResponseRedirect('/')




#registration of an user
def register(request):
    if request.method=='POST':

        form=regForm(request.POST)

        if form.is_valid():
            user=User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            userdata=userDataBase(user=user,
                                  dob=form.cleaned_data['dob'])


            userdata.save()
            #print user.id
            #return HttpResponse('success')
            return redirect('success',i=user.id)
            #return render(request,'success.html',{'name':userdata.user.username})
    else:
        form=regForm()
    return render(request,'reg.html',{'form':form})






