from django.db.models.fields import CharField
from django.shortcuts import render, redirect
from product_app.forms import AddForm, SaleForm, newProductForm
from product_app.models import product, sale, pharmacist, category
from django.contrib.auth.decorators import login_required
from product_app.filters import ProductFilter

# Create your views here.
def home(request):
    products = product.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET, queryset = products)
    products = product_filters.qs

    return render(request, 'products/index.html', {'products': products, 'product_filters': product_filters,})

def availability(self):
        if self.total_quantity >0:
            self.availability = 'Yes'
            return self.availability
        elif self.total_quantity <=0:
            self.availability = 'No'
            return self.availability

def dashboard(request):
    products = product.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET, queryset = products)
    products = product_filters.qs

    return render(request, 'public/index.html', {'products': products, 'product_filters': product_filters,})

def product_detail(request, product_id):
    products = product.objects.get(id = product_id)
    return render(request, 'public/index.html', {'product': products})


@login_required
def receipt(request): 
    sales = sale.objects.all().order_by('-id')
    return render(request, 'products/receipt.html', {'sales': sales,})


def get_total(self):
         total = self.quantity * self.item.unit_price
         return int(total)
def get_change(self):
         change = self.get_total() - self.amount_received
         return abs(int(change))

def all_sales(request):
    sales = sale.objects.all()
    total  = sum([items.amount_received for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request, 'products/all_sales.html',{
     'sales': sales, 'total': total, 'change': change, 'net': net,
    })


@login_required
def product_detail(request, product_id):
    products = product.objects.get(id = product_id)
    return render(request, 'products/product_detail.html', {'product': products})


@login_required
def receipt_detail(request, receipt_id):
    receipt = sale.objects.get(id = receipt_id)
    return render(request, 'products/receipt_detail.html', {'receipt': receipt})


@login_required
def issue_item(request, pk):
    issued_item = product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)  

    if request.method == 'POST':     
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price   
            new_sale.save()
            #To keep track of the stock remaining after sales
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)

            return redirect('receipt') 

    return render (request, 'products/issue_item.html',{'sales_form': sales_form,})
    

@login_required
def add_to_stock(request, pk):
    issued_item = product.objects.get(id = pk)
    form = AddForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()

            #To add to the remaining stock quantity is reducing
            print(added_quantity)
            print (issued_item.total_quantity)
            return redirect('home')

    return render (request, 'products/add_to_stock.html', {'form': form})

@login_required
def new_stock(request):
    new_item = product.objects.all()
    form = newProductForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            new_item.item_name = CharField(request.POST['item_name'])
            new_item.category_name = CharField(request.POST['category_name'])
            new_item.quantity = int(request.POST['quantity'])
            new_item.unit_price = int(request.POST['unit_price'])

            return redirect('home')

    return render (request, 'products/new_stock.html', {'form': form})

 
