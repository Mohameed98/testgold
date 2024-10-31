# Create your views here.
# datasetapp/views.py
from django.shortcuts import render
from .forms import DateRangeForm

def date_input_view(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            # احصل على القيم المدخلة
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            # هنا سيكون الجزء الخاص بمعالجة التواريخ
    else:
        form = DateRangeForm()

    return render(request, 'datasetapp/date_input.html', {'form': form})

