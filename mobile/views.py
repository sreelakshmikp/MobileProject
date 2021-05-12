from django.shortcuts import render,redirect
from .models import Product,Order,Cart
from .forms import CreateProductForm
from .forms import UserRegistrationForm,LoginForm,OrderForm,CartForm
from django.contrib.auth import authenticate,login,logout
from .decorators import login_required,admin_only
# Create your views here.
def index(request):
    return render(request,"mobile/base.html")


@login_required
def list_mobiles(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

@admin_only
def add_product(request):
    form=CreateProductForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreateProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request,"mobile/createmobile.html",context)

def get_mobile_object(id):
    return Product.objects.get(id=id)

@login_required
def mobile_detail(request,id):
    mobile=get_mobile_object(id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)

@admin_only
def mobile_delete(request,id):
    mobile = get_mobile_object(id)
    mobile.delete()
    return redirect("index")

@admin_only
def update(request,id):
    mobile = get_mobile_object(id)
    form = CreateProductForm(instance=mobile)
    context = {}
    context["form"] = form
    if request.method=="POST":
        form=CreateProductForm(instance=mobile,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "mobile/mobileupdate.html", context)

def registration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"mobile/login.html")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
            return redirect("userlogin")
    return render(request,"mobile/registration.html",context)

def login_user(request):
    context={}
    form=LoginForm()
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"mobile/base.html")
        else:
            context["form"]=form
            return render(request,"mobile/login.html",context)
    return render(request,"mobile/login.html",context)

def signout(request):
    logout(request)
    return redirect("userlogin")

@login_required
def item_order(request,id):
    product=get_mobile_object(id)
    form=OrderForm(initial={'user':request.user,'product':product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            context["form"]=form
            return render(request,"mobile/ordereditem.html",context)
    return render(request,"mobile/ordereditem.html",context)

@login_required
def view_my_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"mobile/vieworders.html",context)

@login_required
def order_cancel(request,id):
    order=Order.objects.get(id=id)
    order.status="cancelled"
    order.save()
    return redirect("vieworder")

@login_required
def add_to_cart(request,id):
    product = get_mobile_object(id)
    form = CartForm(initial={'user':request.user,'product':product})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context["form"] = form
            return render(request, "mobile/cartitem.html", context)
    return render(request, "mobile/cartitem.html", context)

@login_required
def view_my_cart(request):
    carts = Cart.objects.filter(user=request.user)
    context = {}
    context['carts'] = carts
    return render(request, 'mobile/viewcart.html', context)

@login_required
def delete_cart_item(request,id):
    carts = Cart.objects.get(id=id)
    carts.delete()
    return redirect('viewcart')

@login_required
def cart_order(request,id):
    carts=Cart.objects.get(id=id)
    form=OrderForm(initial={'user':request.user,'product':carts.product})
    context={}
    context['form']=form
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            delete_cart_item(request,id)
            return redirect('viewcart')
        else:
            context['form']=form
            return render(request,'mobile/ordereditem.html',context)
    return render(request, 'mobile/ordereditem.html', context)


