from django.shortcuts import render


def login_page(request):
    return render(request, 'login/login_page.html')

