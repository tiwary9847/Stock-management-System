from django.shortcuts import render,redirect
from .models import Stock
from .forms import StockCreateForm,StockSearchForm,StockUpdateForm

# Create your views here.
def home(request):
	title = 'Welcome to Stock management'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def list_items(request):
	title = 'List of Items'
    #form=StockSearchForm(request.POST or None)
    
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_item.html", context)


def add_items(request):
    form=StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')

    context={
        "form":form,
        "title":"Add Item"
    }
    return render(request,"add_items.html",context)

def Update_items(request,pk):
    queryset = Stock.objects.get(id=pk)
    form=StockUpdateForm(instance=queryset)
    if request.method=='POST':
        form=StockUpdateForm(request.POST,instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')
    
    context={
        'form':form
    }
    return render(request,'add_items.html',context)

def delete_items(request, pk):
    queryset = Stock.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/list_items')
    return render(request, 'delete_items.html')





