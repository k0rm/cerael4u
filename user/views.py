from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from user.forms.profile_form import ProfileForm
from user.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False) # Gert til að commita ekki í gagnagrunninn því FK er ekki implementaður en gerir temp profile
            profile.user = request.user      #tengir við innskráðan notanda
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
            'form': ProfileForm(instance=profile)
        })