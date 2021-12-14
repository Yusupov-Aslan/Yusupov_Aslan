from django.shortcuts import render


# Create your views here.

def index_view(request):
    return render(request, "index.html")


def add_view(request):
    if request.method == "POST":
        display_type = request.POST.get("calculate_type", None)
        if display_type in ["add"]:
            num1 = request.POST.get('num1', None)
            num2 = request.POST.get('num2', None)
            if num1.isdigit() and num2.isdigit():
                a = int(num1)
                b = int(num2)
                res = a + b
                result = f"{a} + {b} = {res}"
                return render(request, "result.html", {"result": result})
            else:
                res = "Only digits are allowed"
                return render(request, "result.html", {"result": res})
        elif display_type in ["subtract"]:
            num1 = request.POST.get('num1', None)
            num2 = request.POST.get('num2', None)
            if num1.isdigit() and num2.isdigit():
                a = int(num1)
                b = int(num2)
                res = a - b
                result = f"{a} - {b} = {res}"
                return render(request, "result.html", {"result": result})
            else:
                res = "Only digits are allowed"
                return render(request, "result.html", {"result": res})
        elif display_type in ["multiply"]:
            num1 = request.POST.get('num1', None)
            num2 = request.POST.get('num2', None)
            if num1.isdigit() and num2.isdigit():
                a = int(num1)
                b = int(num2)
                res = a * b
                result = f"{a} * {b} = {res}"
                return render(request, "result.html", {"result": result})
            else:
                res = "Only digits are allowed"
                return render(request, "result.html", {"result": res})
        elif display_type in ["divide"]:
            num1 = request.POST.get('num1', None)
            num2 = request.POST.get('num2', None)
            if num1.isdigit() and num2.isdigit():
                a = int(num1)
                b = int(num2)
                if b == 0:
                    res = "Zero divide error"
                    return render(request, "result.html", {"result": res})
                else:
                    res = a / b
                    result = f"{a} / {b} = {res}"
                    return render(request, "result.html", {"result": result})
            else:
                res = "Only digits are allowed"
                return render(request, "result.html", {"result": res})
    else:
        return render(request, "result.html")
