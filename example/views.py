

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from HackathonAI2023 import main


def czat(request):
    return render(request, 'czat.html')


@csrf_exempt
def odpowiedz(request):
    if request.method == 'POST':
        pytanie = request.POST.get('pytanie')

        odpowiedz = main.run_agent(pytanie)

        print(odpowiedz)

        return JsonResponse({'odpowiedz': odpowiedz})
    else:
        return JsonResponse({'error': 'Nieprawidłowe żądanie'})