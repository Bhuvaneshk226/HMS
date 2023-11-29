from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.views import LogoutView
# Create your views here.
def homepage(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('school_cards')
    else:
        return render(request,'index.html')

@staff_member_required
def dashboard(request):
    return render(request,'dashboard.html')

@staff_member_required
def school_cards(request):
    return render(request,'school_cards.html')

@staff_member_required
def school_add(request):
    return render(request,'school_add.html')

@staff_member_required
def Teachers(request):
    return render(request,'Teachers.html')

@staff_member_required
def Transport(request):
    return render(request,'Transport.html')

@staff_member_required
def Accounts(request):
    return render(request,'Accounts.html')
