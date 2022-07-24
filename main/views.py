from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import is_valid_path
from .forms import CreateNewList
from .models import ToDoList, Item
# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
#Pega cada item do checkbox, e adiciona o ID como string, para identificar unicamente
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                    
            item.save()
                
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid input")
    
    
    return render(response, "main/list.html", {"ls":ls})
 
def home(response):
    return render(response, "main/home.html", {})

def create(response):
    #Pega od dados do formulário enviado via post e salva na nova lista
    if response.method == "POST":
        form = CreateNewList(response.POST)
    #Verifica os dados e limpa e salva o nome da lista    
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            
     #Depois de salvar, redireciona para a lista recém criada, passando o ID       
            
            return HttpResponseRedirect("/%i" %t.id)

    else: 
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})
