from django import forms
from django.db import models
from coa.models import coaEntry

class CoaForms(forms.ModelForm):
    facility = models.CharField(max_length=10)
    enteringUser = models.CharField(max_length=10)

    # these will be filled in from the question back
    questionOne = models.CharField( max_length=1000, editable=False)
    questionTwo = models.CharField(max_length=1000, editable=False)
    questionThree = models.CharField(max_length=1000)

    # these are the fields entered
    askedUser = models.CharField(max_length=10)
    answerOne = models.CharField(max_length=1000)
    answerTwo = models.CharField(max_length=1000)
    answerThree = models.CharField(max_length=1000)

    class Meta:
        model = coaEntry
        fields = ('enteringUser', 'askedUser', 'facility', 'questionOne', 'answerOne', 'questionTwo', 'answerTwo', 'questionThree', 'answerThree' )
