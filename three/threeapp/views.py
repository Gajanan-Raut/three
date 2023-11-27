from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from threeapp.models import Task,Course
from threeapp.form import EmpRegister,Emp,stud
from threeapp.form import CourseForm
from threeapp.form import EmpRegister,CourseForm,RegisterForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return HttpResponse('hello django')
def about(request):
    content={}
    #content['data']=Task.objects.all()
    user_id=request.user.id
    Q1=Q(is_deletes='N')
    Q2=Q(uid=user_id)
    content['data']=Task.objects.filter(Q1&Q2)


   
    return render(request,'about.html',content)
def create(request):
    if request.method=='POST':
        t=request.POST['t']
        det=request.POST['det']
        dt=request.POST['dt']
        user_id=request.user.id

        print(user_id)

        t1=Task.objects.create(title=t,details=det,date=dt,uid=user_id,is_deletes='N')
        t1.save()
        #print(t1)
        
        
        return redirect('/about')
    else:

        return render(request,'create.html')
    
def delete(request,n):
    #x=Task.objects.filter(id=n)
    #x.delete()

    x=Task.objects.filter(id=n)
    x.update(is_deletes='Y')
    return redirect('/about')
# def edit(request,n):
#     if request.method=='POST':
#         ut=request.POST['t']
#         udet=request.POST['det']
#         udt=request.POST['dt']
        
        
#         x=Task.objects.filter(id=n)
#         x.update(title=ut,details=udet,date=udt)
#         return redirect('/about')
#     else:
#         content={}
#         content['data']=Task.objects.filter(id=n)
    
#         return render(request,'edit.html',content)
    
def dashboard(request):
    content={}
    #content['data']=Course.ccustomobj.all()
    #content['data']=Course.obj.all()
    #content['data']=Course.objects.filter(ccat='developement')
    #content['data']=Course.objects.filter(ccat='Data Science')
    #content['data']=Course.objects.filter(cprice__gt=20000)
    #content['data']=Course.objects.filter(ccat='Data Science',cprice__gt=20000)

    #Q1=Q(cprice__gt=20000)
    #Q2=Q(ccat='Data Science')
    #Q3=Q()

    #content['data']=Course.objects.filter(Q3|Q1|Q2)
    #content['data']=Course.objects.order_by('cdur')
    #content['data']=Course.objects.order_by('-cdur')
    content['data']=Course.ccustomobj.sortfeeshightolowds()

    return render(request,'dashboard.html',content)

def htol(request):
    content={}
    content['data']=Course.objects.order_by('cdur').order_by('-cprice')
    return render(request,'dashboard.html',content)

def ltoh(request):
    content={}
    content['data']=Course.objects.order_by('-cdur').order_by('cprice')
    return render(request,'dashboard.html',content)

def showform(request):
    content={}
    fobj=EmpRegister()
    content['form']=fobj
    return render(request,'empregister.html',content)

def show(request):
    content={}
    obj=Emp()
    content['f']=obj
    return render(request,'emp.html',content)

def stu(request):
    ob=stud
    return render(request,'stu.html',{'stu':ob})

def showmodelform(request):
    mfobj=CourseForm()
    content={}
    content['form']=mfobj
    return render(request,'CreateCourse.html',content)

class MyView(View):
    def get(self,request):

        return HttpResponse("hello from myviews with get request")
    
    def post(self,request):
        cname=request.POST['Course_name']
        cdur=request.POST['Course_duration']
        ccat=request.POST['Course_category']
        cfees=request.POST['Course_fees']
        print(cname)
        print(cdur)
        print(ccat)
        print(cfees)

        return HttpResponse("hello form myview,with post")
'''   
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        pass1=request.POST['password1']
        #print(uname)
        #print(pass1)
        u1=User(username=uname,password=pass1,is_staff=True,is_active=True)
        u1.save()
        return redirect('/register')
    else:
        fm=UserCreationForm()
        return render(request,'signup.html',{'form':fm})
    '''
'''
def register(request):
    if request.method=='POST':
        fm=UserCreationForm(request.POST)
        #print(fm)
        print(fm.is_valid())
        if fm. is_valid():
            fm.save()
        return redirect('/register')
    else:
        fm=UserCreationForm()
        return render(request,'signup.html',{'form':fm})

        '''

def register(request):
    if request.method=='POST':
        fm=RegisterForm(request.POST)
        #print(fm)
        #print(fm.is_valid())
        if fm.is_valid():
            messages.success(request,'Account Created Successfully,please login!!!')
            fm.save()
        return redirect('/register')
    else:
        fm=RegisterForm()
        return render(request,'signup.html',{'form':fm})
def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        #print(fm)
        #print(fm.is_valid())

        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']

            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u:
                login(request,u)
                return redirect('/about')





        #return HttpResponse('in post section')

    else:
        fm=AuthenticationForm()

    return render(request,'login.html',{'form':fm})


def user_logout(request):
    logout(request)
    return redirect('/login')

def setcookie(request):
    r=render(request,'setcookie.html')
    r.set_cookie('name','Itvedant')
    #r.set_cookie('name','Itvedant Eclass',max_age=60)
    return r

def getcookie(request):
    #d=request.COOKIES['name']
    #d=request.COOKIES.get('name')
    d=request.COOKIES.get('name','helllo guest')
    return render(request,'getcookie.html',{'data':d})

def setsession(request):
    request.session['user']="ITVEDANT USER"
    return render(request,'setsession.html')

def getsession(request):
    d=request.session['user']

    return render(request,'getsession.html',{'data':d})

def del_session(request):
    if 'user' in request.session:
        del request.session['user']
        return HttpResponse("Session Deketed!!!!")
    

def getloggeduserid(request):
    user_id=request.user.id
    return render(request,'getsession.html',{'data':user_id})
    


