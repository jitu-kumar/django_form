from django.shortcuts import render

from .models import JeetuModel
from .forms import JeetuForm
# Create your views here.


def home_view(request):
    form = JeetuForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'home.html', {'form': form})
