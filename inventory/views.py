from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Prefetch
from inventory.models import Medicine, Stock, Sell  # Import your models
from inventory.forms import MedicineForm

def home(request):
    return render(request, 'inventory/home.html')
def home(request):
    """Render the home page of the Medical Shop Management System."""
    return HttpResponse("Welcome to the Medical Shop Management System!")

def medicines_list(request):
    """Display a list of all medicines."""
    medicines = Medicine.objects.all()
    return render(request, 'inventory/medicines_list.html', {'medicines': medicines})

def stocks_list(request):
    """Display a list of all stocks."""
    stocks = Stock.objects.all()
    return render(request, 'inventory/stocks_list.html', {'stocks': stocks})

def sales_list(request):
    """Display a list of all sales."""
    sales = Sell.objects.all()  # Fixed: changed Sale to Sell
    return render(request, 'inventory/sales_list.html', {'sales': sales})

def inventory_list(request):
    """Display inventory items with stock and sales information."""
    medicines = Medicine.objects.prefetch_related(
        Prefetch('stocks', queryset=Stock.objects.all()),  # Use related_name from the model
        Prefetch('sales', queryset=Sell.objects.all())
    )

    inventory_items = [
        {
            'medicine': medicine,
            'stock': medicine.stocks.first(),  # Get the latest related stock item
            'sold_count': medicine.sales.count()  # Count how many sold
        }
        for medicine in medicines
    ]

    return render(request, 'inventory/inventory_list.html', {'inventory_items': inventory_items})

def add_medicine(request):
    """Add a new medicine to the inventory."""
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'inventory/add_medicine.html', {'form': form})

def update_medicine(request, pk):
    """Update an existing medicine."""
    medicine = get_object_or_404(Medicine, pk=pk)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'inventory/update_medicine.html', {'form': form})
