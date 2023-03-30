from django.shortcuts import render

def register_view(request):
    return render(request, 'authors/register_view.html')