from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView, DeleteView

# Define the home view
def home(request):
    item_list = Item.objects.all()
    return render(request, 'index.html', { 'item_list' : item_list })

class ItemCreate(CreateView):
    model = Item
    fields = '__all__'

class ItemDelete(DeleteView):
    model = Item
    success_url = '/'