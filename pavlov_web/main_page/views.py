from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# Create your views here.
def test(request):
    return render(request, 'main_page/main.html')
def tester():
    pass
