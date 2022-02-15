

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_login.forms import SignUpForm,UserChangeProfile,ChangeProfilePicture



# Create your views here.


def sign_up(request):
    form=SignUpForm()
    registered=False
    if request.method=='POST':
        form=SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True  
    dict={'form':form, 'registered':registered}
    return render(request, 'App_login/sign_up.html',context=dict)

def user_login(request):
    form= AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get('username')
            user_password=form.cleaned_data.get('password')
            user=authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_login/login.html', context={'form':form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def user_profile(request):
    return render(request, 'App_Login/profile.html',context={})     


@login_required
def user_change_profile(request):
    current_user=request.user
    form=UserChangeProfile(instance=current_user)
    if request.method == 'POST':
        form=UserChangeProfile(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:profile'))
            #form=UserChangeProfile(instance=current_user)
    return render(request, 'App_login/edit_profile.html', context={'form':form})




@login_required
def change_password(request):
    current_user=request.user
    success=False
    form=SetPasswordForm(current_user)
    if request.method == 'POST':
        form=SetPasswordForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            success=True
    return render(request,'App_login/change_password.html',context={'form':form, 'success':success})


@login_required
def set_profile_pic(request):
    form = ChangeProfilePicture()
    if request.method == 'POST':
        form = ChangeProfilePicture(request.POST, request.FILES)
        if form.is_valid():
            user_object=form.save(commit=False)
            user_object.user=request.user
            user_object.save()
            return HttpResponseRedirect(reverse('App_login:profile'))

    return render(request, 'App_Login/add_profile_picture.html',context={'form':form})

@login_required
def update_profile_pic(request):
    
    form = ChangeProfilePicture(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ChangeProfilePicture(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_Login/add_profile_picture.html',context={'form':form})
