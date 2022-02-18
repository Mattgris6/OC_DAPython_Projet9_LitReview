from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from django.shortcuts import get_object_or_404

@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'flux/home.html', context={'tickets': tickets})

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
        
