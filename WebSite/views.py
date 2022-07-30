from django.shortcuts import render, redirect
from .models import ApplicationRandomModel
from datetime import datetime
import random
import uuid

def index(request):
    template_name = 'WebSite/index.html'
    
    if request.POST:
        try:
            _datetime  = request.POST.get('appt')
            min_range = request.POST.get('min')
            max_range = request.POST.get('max')
            client_time = request.POST.get('date-time')
            random_number = random.randint(int(min_range), int(max_range))
            _model = ApplicationRandomModel.objects.create(date_close=datetime.strptime(_datetime, '%Y-%m-%dT%H:%M'), 
            date_open=datetime.strptime(client_time, '%Y-%m-%dT%H:%M:%S.%f%z'), 
            result=str(random_number),
            generated_amount=1, unique_url=uuid.uuid4().hex,
            _range= f"From {min_range} To {max_range}")
            
            return redirect(f'share/{_model.unique_url}')
        
        except Exception as e:
            print(e)
            return redirect('/')
    
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
