

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def czat(request):
    return render(request, 'czat.html')

@csrf_exempt
def odpowiedz(request):
    if request.method == 'POST':
        pytanie = request.POST.get('pytanie')

        # Tutaj można dodać logikę odpowiedzi na pytanie
        odpowiedz = f'Odpowiedź na pytanie: "{pytanie}"'

        return JsonResponse({'odpowiedz': odpowiedz})
    else:
        return JsonResponse({'error': 'Nieprawidłowe żądanie'})
