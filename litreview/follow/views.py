from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.conf import settings
from django.contrib.auth import get_user_model
User=get_user_model()

@login_required
def follow_user(request):
    users = User.objects.all()
    following_users = models.UserFollows.objects.filter(followed_user=request.user)
    followed_users = models.UserFollows.objects.filter(user=request.user)
    form = forms.UserFollowsForm()
    list_of_user = []
    for elem in users:
        if elem != request.user:
            list_of_user.append(elem)
    if request.method == 'POST':
        form = forms.UserFollowsForm(request.POST)
        print(form)
        if form.is_valid():
            new_follower = form.save(commit=False)
            # set the uploader to the user before saving the model
            new_follower.followed_user = request.user
            # now we can save
            new_follower.save()
            return redirect('follow_manager')
    return render(request,
                    'follow/follow_manager.html',
                    {'form':form,
                    'users': list_of_user,
                    'following_users':following_users,
                    'followed_users':followed_users,
                    })