from django.shortcuts import render, redirect, render_to_response
import getpass
from .forms import CoaForms
from datetime import datetime, timedelta
from .models import facilityGoal, coaEntry, coaQuestionBank
from django.template import RequestContext
from django_tables2 import RequestConfig
from .tables import coaEntryTable

# Create your views here.

def coa_home(request):
    if 'facility' not in request.session:
        return redirect('/')

    startOfWeekDate = (datetime.today() - timedelta(days = (1 + datetime.today().weekday())))
    coasWeekToDate = coaEntry.objects.filter(dateEntered__gte=startOfWeekDate, facility=request.session['facility']).count()
    try:
        facilityGoalAmount = getattr(facilityGoal.objects.get(goalType= 'COA', facility=request.session['facility']),"goalAmount")
    except facilityGoal.DoesNotExist:
        facilityGoalAmount = "0"

    coaTable = coaEntryTable(coaEntry.objects.filter(dateEntered__gte=startOfWeekDate, facility=request.session['facility']))
    RequestConfig(request).configure(coaTable)

    context = {
        'userName': request.session['username'],
        'facility': request.session['facility'],
        'coaPercent':  str(coasWeekToDate) ,
        'coaWeekToDate': str(coasWeekToDate),
        'coaGoal': str(facilityGoalAmount),
        'coaTable': coaTable,
    }

    return render(request, 'coaMain.html', context)


def add_coa(request):
    if 'facility' not in request.session:
        return redirect('/')

    # Get the context from the request.
    context = RequestContext(request)

    if request.method == 'POST':
        form = CoaForms(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect('/coa/')

    else:
        # If the request was not a POST, display the form to enter details.
        form = CoaForms(initial={'enteringUser': getpass.getuser(),
                                 'facility': request.session['facility'],
                                 'questionOne': getattr(coaQuestionBank.objects.get(facility=request.session['facility']),"questionOne"),
                                 'questionTwo': getattr(coaQuestionBank.objects.get(facility=request.session['facility']), "questionTwo"),
                                 'questionThree': getattr(coaQuestionBank.objects.get(facility=request.session['facility']), "questionThree"),
                                 })

        # Bad form (or form details), no form supplied...
        # Render the form with error messages (if any).

    return render(request, 'coa_entry.html', {'form': form}, context)
