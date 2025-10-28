from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        user = authenticate(request, email=mail, password=password)
        if user is not None:
            login(request,user)
            return redirect('shop')
    return render(request,'login.html')

def create_account_view(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = reqest.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password!=confirm_password:
            message.error(request,'passwords donot match.')
            return render(request,'create_account.html')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists.")
            return render(request,'create_account.html')
        user = User.objects.create_user(username=username,mail=mail,password=password)
        user.save()
        messages.success(request,f"Account created for {suername}")
        return redirect ('login')
    return render(request,'create_account.html')


def logout(request):
    pass
def profile(request):
    return render(request,'profile.html')
def custom_404(request,exception):
    return render(request,'404.html',status=404)

# Create your views here.
