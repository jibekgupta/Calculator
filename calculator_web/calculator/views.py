from django.shortcuts import render
from django.http import JsonResponse

def calculator(request):
    result = ""
    if request.method == "POST":
        expression = request.POST.get('expression')
        try:
            result = eval(expression)
        except:
            result = "ERROR"
        return JsonResponse(result, safe=False)

    return render(request, 'calculator/calculator.html', {'result': result})
