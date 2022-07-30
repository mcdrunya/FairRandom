from django.shortcuts import render, redirect
from .models import ApplicationRandomModel
from datetime import datetime
import pytz
import random
import uuid
from django.utils import timezone
import datetime

def index(request):
    template_name = 'WebSite/index.html'
    print(timezone.now())  # The UTC time
    print(timezone.localtime())  # timezone specified time, 
    print(datetime.datetime.now())  # default local time
    
    if request.POST:
        _datetime  = request.POST.get('appt')
        min_range = request.POST.get('min')
        max_range = request.POST.get('max')
        random_number = random.randint(int(min_range), int(max_range))
        _model = ApplicationRandomModel.objects.create(date_close=datetime.strptime(_datetime, '%Y-%m-%dT%H:%M'), 
        date_open=datetime.now(), 
        result=str(random_number),
        generated_amount=1, unique_url=uuid.uuid4().hex,
        _range= f"From {min_range} To {max_range}")
        
        return redirect(f'share/{_model.unique_url}')

    return render(request, template_name)


def choose_time(request, url:str):

    _model: ApplicationRandomModel = ApplicationRandomModel.objects.filter(unique_url=url).first()
    if _model:
        return render(request, 'WebSite/show_case.html', {"date_close":_model.date_close, 
        "date_open":_model.date_open, 
        "range":_model._range,
        "result":_model.result})
    else:
        return redirect('/') 


def about(request):
    return render(request, 'WebSite/about.html')


def page_not_found_view(request, exception):
    return render(request, 'WebSite/page_not_found.html', status=404)
