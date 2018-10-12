from django.shortcuts import render

# Create your views here.

def test_homepage(request):
    context = {
    }
    return render(request, 'test_page.html', context)
