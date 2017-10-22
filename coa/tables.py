# tutorial/tables.py
import django_tables2 as tables
from .models import coaEntry

class coaEntryTable(tables.Table):

    class Meta:
        model = coaEntry
        # add class="paleblue" to <table> tag
        attrs = {'class': 'table table-striped'}
        sequence = ('dateEntered','facility', 'enteringUser', 'askedUser')
        exclude=('questionOne','answerOne', 'questionTwo','answerTwo','questionThree','answerThree','id','...')