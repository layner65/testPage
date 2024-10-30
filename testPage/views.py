# testPage/views.py
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("<h1>Welcome to the testPage app!</h1>")