from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.http import HttpResponse

# Create your views here.

def curd(request):
    return render(request, 'curd.html')

def index(request):
    return render(request, 'index.html')

def form_elements(request):
    return render(request, 'form-elements.html')

def form_layout(request):
    a=102
    return render(request, 'form-layout.html')

def hello(request):
    return HttpResponse("Hello, world. You're at the app hello.")



#   Read or show list
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


#       Create date
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})


#           Update data
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})


#            Delete data
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})
