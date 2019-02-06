from django.shortcuts import render

def test(request):
    return render(request, 'tetest.html')

# Create your views here.
