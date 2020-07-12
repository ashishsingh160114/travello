from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.mail import send_mail
from teja import settings

# Create your views here.




def upload(request):
    context={}
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
    return render(request,'upload.html',context)




    
def login(request):
    if request.method=='POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else :
            messages.info(request, 'Username or Password is incoreect... please try again')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method=='POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                sub='travello agency'
                msg='we are glad to inform you that you registered successfully.'
                #to='ashishsingh160114@gmail.com'
                res=send_mail(sub,msg,settings.EMAIL_HOST_USER,[email])
                print('User Created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    
    else :
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request,'about.html')


'''def mail(request):
    sub='hello sir'
    mssg='this is django test mail'
    to='ashishsingh160114@gmail.com'
    res=send_mail(sub,mssg,settings.EMAIL_HOST_USER,[to])
    
    return render(request,'mail.html')'''