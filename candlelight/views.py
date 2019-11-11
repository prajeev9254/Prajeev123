from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'marketing-index.html')
from .models import post





from.models import post


# ob1=post()
# ob1.head='1'
# ob1.desc='qwertu'
# ob1.date='12346'
#
# ob2=post()
# ob2.head='2'
# ob2.desc='qwertu'
# ob2.date='12346'
#
# ob3=post()
# ob3.head='3'
# ob3.desc='qwertu'
# ob3.date='12346'
# objects=[ob1,ob2,ob3]
def index(request):
    objects = post.objects.all()
    recents=post.objects.order_by('-date')[0:3]
    return render(request,'marketing-index.html',{'ob': objects,'re':recents})
def web(request):
    if request.method=='POST':
         a=request.POST['username']
         b=request.POST['password']
         print(request.POST)
         # return render(request,'base.html')
         user = auth.authenticate(username=a, password=b)
         if user is not None:
             auth.login(request, user)
             return redirect('candlelight:home')
         else:
             messages.error(request,'please check ur username or password')
                # print('error')
         return redirect('candlelight:login')

    return render(request,'login.html')
def myy(request):
    auth.logout(request)
    # return render(request,'logout.html')
    return redirect('candlelight:home')
def reg(request):
    return render(request,'registration.html')
def regg(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['first name']
        c = request.POST['last name']
        d = request.POST['email']
        e = request.POST['psw']
        f = request.POST['psw-repeat']
        if e == f:
                if User.objects.filter(username=a).exists():
                    messages.error(request,'user name is used')
                    return redirect('candlelight:register')
                elif User.objects.filter(email=d).exists():
                    messages.error(request,'email id exist')
                    return redirect('candlelight:register')
                else:
                    v=User.objects.create_superuser(username=a,first_name=b,last_name=c,email=d,password=e,is_superuser=False,is_staff=True)
                    v.save()
                    auth.login(request,v)
        else:
            messages.error(request,'error')
            return redirect('candlelight:register')
        return redirect('candlelight:home')
    return render(request, 'registration.html')

def index(request):
    object_list = post.objects.all()
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return render(request, 'marketing-index.html', {'contacts': objects})

