from django.shortcuts import render, HttpResponse


def home(request):
    name = 'Duncan Moyo'
    numbers = [1, 2, 3, 4, 5]

    context = {
        'my_name': name,
        'my_numbers': numbers,
    }
    return render(request, 'accounts/login.html', context)
