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
    following_users = models.UserFollows.objects.filter(followed_user=request.user).prefetch_related('user')
    followed_users = models.UserFollows.objects.filter(user=request.user).prefetch_related('followed_user')   
    if request.method == 'POST':
        u_name = request.POST.get('id_user', None)
        u_follower = User.objects.get(username=u_name)
        if u_follower != request.user:
            new_followed = models.UserFollows()
            new_followed.followed_user = request.user
            new_followed.user = u_follower
            # now we can save
            try:
                new_followed.save()
            except:
                pass
        return redirect('follow_manager')
    return render(request,
                    'follow/follow_manager.html',
                    {#'form':form,
                    'following_users':following_users,
                    'followed_users':followed_users,
                    'users':users,
                    })

def unfollow(request, follow_id):
    follow = models.UserFollows.objects.get(id=follow_id)
    
    if request.method == 'POST':
        follow.delete()
        return redirect('follow_manager')
    return render(request,
                    'follow/unfollow.html',
                    {'follow': follow})