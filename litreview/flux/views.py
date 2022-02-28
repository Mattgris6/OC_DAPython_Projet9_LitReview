from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.shortcuts import get_object_or_404

from itertools import chain

from django.db.models import CharField, Value


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = models.Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets_done = [review.ticket for review in reviews]
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    context={
        'posts': posts,
        'tickets_done': tickets_done
    }
    return render(request, 'flux/home.html', context)

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
        'ticket_form':ticket_form,
        'review_form':review_form,
    }
    return render(request, 'flux/review_upload.html', context=context)
        
@login_required
def review_answer(request, ticket_id):
    ticket = models.Ticket.objects.get(id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
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
        'ticket':ticket,
        'review_form':review_form,
    }
    return render(request, 'flux/review_answer.html', context=context)
        