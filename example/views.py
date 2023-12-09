

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from HackathonAI2023 import main
from django.http import HttpResponse


def czat(request):
    return render(request, 'czat.html')

def pytanie(request):
    #pytanie = request.POST.get('pytanie')
    pytanie = "dodaj mi do klasy computer parametr aabcd"
    return pytanie



@csrf_exempt
def odpowiedz(request):
    if request.method == 'POST':
        pytanie = request.POST.get('pytanie')

        odpowiedz = main.ask_openai_question(pytanie)
        ai_message = odpowiedz.get('result', '')

        # Include both AI Message and the confirmation message in the JSON response
        #return JsonResponse({'odpowiedz': ai_message, 'confirmation': 'okey i changed it'})
        return JsonResponse({'odpowiedz' : 'dobra ryju ogarnelem to'})
    else:
        return JsonResponse({'error': 'Nieprawidłowe żądanie'})