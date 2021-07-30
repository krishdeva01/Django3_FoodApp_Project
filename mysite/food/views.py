from django.db import models
from .forms import ItemForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.views.generic import ListView,DetailView,CreateView


class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'items'
    

def item(request):
    return HttpResponse("Hi im Krish Anjel")
   

class DetailClassView(DetailView):
    model = Item
    template_name = 'food/detail.html'
   

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form})
#this is a class based item for create item

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)



def update_item(request,id):
    item = Item.objects.get(id= id)
    form = ItemForm(request.POST or None,instance= item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id = id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item-delete.html',{'item':item})

    