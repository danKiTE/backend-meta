from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content)

def qryview(request):
    name = request.GET["name"]
    id = request.GET["id"]
    return HttpResponse("Name: {}, id: {}".format(name, id))

def showform(request): 
    return render(request, "form.html") 
def menuitems(request, dish):
    items ={
        "pasta":"Ngon",
        "dispasta": "ko ngon"
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} <h2>" + description)

def drinks(request, drink_name):
    items = {
        "mocha":"type of coffee",
        "tea":"type of begavera",
        "lemonnade":"type of refreshment"
    }
    description = items[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2>" + description)
