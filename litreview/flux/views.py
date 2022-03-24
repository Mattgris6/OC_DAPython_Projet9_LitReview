from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models

from itertools import chain

from django.db.models import CharField, Value, Q
from follow.models import UserFollows


def get_users_viewable_tickets(this_user):
    usersfollows = UserFollows.objects.filter(followed_user=this_user)
    user_follow_list = [this_user]
    for users in usersfollows:
        user_follow_list.append(users.user)
    ticket = models.Ticket.objects.all().filter(user__in=user_follow_list)
    return ticket


def get_users_viewable_reviews(this_user):
    my_tickets = models.Ticket.objects.filter(user=this_user)
    usersfollows = UserFollows.objects.filter(followed_user=this_user)
    user_follow_list = [this_user]
    for users in usersfollows:
        user_follow_list.append(users.user)
    reviews = models.Review.objects.all().filter(
        Q(user__in=user_follow_list) | Q(ticket__in=my_tickets)
        )
    return reviews


@login_required
def home(request):
    tickets = get_users_viewable_tickets(request.user)
    tickets = tickets.annotate(
        content_type=Value('TICKET', CharField()),
        page_type=Value('FLUX', CharField())
        )
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(
        content_type=Value('REVIEW', CharField()),
        page_type=Value('FLUX', CharField())
        )
    tickets_done = [review.ticket for review in reviews]
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    context = {
        'posts': posts,
        'tickets_done': tickets_done
    }
    return render(request, 'flux/home.html', context)


@login_required
def own_posts(request):
    current_user = request.user
    tickets = models.Ticket.objects.filter(user=current_user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    tickets = tickets.annotate(page_type=Value('POSTS', CharField()))
    reviews = models.Review.objects.filter(user=current_user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    reviews = reviews.annotate(page_type=Value('POSTS', CharField()))
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )
    context = {
        'posts': posts,
    }
    return render(request, 'flux/own_posts.html', context)


@login_required
def ticket_delete(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('own_posts')
    return render(
        request,
        'flux/post_delete.html',
        {'ticket': ticket}
        )


@login_required
def review_delete(request, review_id):
    review = models.Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('own_posts')
    return render(
        request,
        'flux/post_delete.html',
        {'review': review}
        )


@login_required
def ticket_update(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('own_posts')
    else:
        form = forms.TicketForm(instance=ticket)
    return render(
        request,
        'flux/ticket_upload.html',
        {'form': form}
        )


@login_required
def review_update(request, review_id):
    review = models.Review.objects.get(id=review_id)
    ticket = review.ticket
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            # now we can save
            review.save()
            return redirect('own_posts')
    else:
        review_form = forms.ReviewForm(instance=review)
    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(
        request,
        'flux/review_answer.html',
        context
        )


@login_required
def ticket_upload(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            return redirect('home')
    return render(request, 'flux/ticket_upload.html', context={'form': form})


@login_required
def review_upload(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            review = review_form.save(commit=False)
            # set the uploader to the user before saving the model
            review.user = request.user
            review.ticket = ticket
            # now we can save
            review.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'flux/review_upload.html', context=context)


@login_required
def review_answer(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            # set the uploader to the user before saving the model
            review.user = request.user
            review.ticket = ticket
            # now we can save
            review.save()
            return redirect('home')
    context = {
        'ticket': ticket,
        'review_form': review_form,
    }
    return render(request, 'flux/review_answer.html', context=context)
