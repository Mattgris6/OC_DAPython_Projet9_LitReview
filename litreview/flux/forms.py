from django import forms

from . import models


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    title = forms.CharField(label='Titre', max_length=128, widget=forms.TextInput(attrs={'size': '60'}))
    description = forms.CharField(label='Description', max_length=2048, required=False, widget=forms.Textarea(attrs={'rows': '10', 'cols': '60'}))
    image = forms.ImageField(label='Image', required=False)
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    RATINGS = [('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    headline = forms.CharField(label='Titre', max_length=128, widget=forms.TextInput(attrs={'size': '60'}))
    rating = forms.ChoiceField(label='Note', widget=forms.RadioSelect, choices=RATINGS)
    body = forms.CharField(label='Commentaire', max_length=8192, required=False,
                           widget=forms.Textarea(attrs={'rows': '10', 'cols': '60'}))
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
