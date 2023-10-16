import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



from .models import *

STATUS = ["Pending", "Delivered", "Out For Delivery"]
CATEGORIES = ["Outdoor", "Indoor"]


@login_required
def dashboard(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all().order_by('-date_ordered')
    orders_delivered = Order.objects.filter(status="Delivered").count()
    orders_pending = Order.objects.filter(status="Pending").count()


    return render(request, "app/dashboard.html", {
        "customers": customers,
        "products": products,
        "status": STATUS,
        "orders": orders,
        "orders_delivered": orders_delivered,
        "orders_pending": orders_pending
    })


@login_required
def products(request):
    if request.method == "POST":
        name = request.POST["name"]
        price = request.POST["price"]
        category = request.POST["category"]

        Product.objects.create(name=name, price=price, category=category)
        messages.success(request, "Product Added Successfully")
        return redirect('products')
    else:
        products = Product.objects.all()
        return render(request, "app/products.html", {
            "products": products,
            "categories": CATEGORIES
        })


@login_required
def customer(request):
    name = request.POST["name"]
    phone = request.POST["phone"]
    email = request.POST["email"]

    Customer.objects.create(name=name, phone=phone, email=email)
    messages.success(request, "Customer Added Successfully")
    return redirect('dashboard')
       


@login_required
def place_order(request):
    if request.method == "POST":
        product = Product.objects.get(id=request.POST["product"])
        customer = Customer.objects.get(id=request.POST["customer"])
        status = request.POST["status"]

        Order.objects.create(product=product, customer=customer, status=status)
        messages.success(request, "Order placed successfully")
        return redirect("dashboard")
    else:
        pass

@csrf_exempt
@login_required
def customer_page(request, id):
    customer = Customer.objects.get(id=id)
    orders = Order.objects.filter(customer=customer)

    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]

        Customer.objects.filter(id=id).update(name=name, phone=phone, email=email)

        messages.success(request, "Customer Updated Successfuly!")

        return redirect("customer_page", id)
    else:
        return render(request, "app/customer.html", {
            "customer": customer,
            "orders": orders,
            "status": STATUS,
            "categories": CATEGORIES
        })


@login_required
def delete_customer(request, id):
    Customer.objects.filter(id=id).delete()
    messages.success(request, "Customer deleted successfully")
    return redirect("dashboard")


@login_required
def order(request, id):

    # Return order contents
    if request.method == "GET":
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found."}, status=404)

        return JsonResponse(order.serialize())
    elif request.method == "POST":
        product = Product.objects.get(id=request.POST['product'])
        customer = Customer.objects.get(id=request.POST['customer'])
        status = request.POST['status']

        order = Order.objects.filter(id=id)
        order.update(product=product, customer=customer, status=status)

        messages.success(request, "Order Updated Successfully")

        return redirect('dashboard')

@login_required
def delete_order(request, id):
    Order.objects.filter(id=id).delete()
    messages.success(request, "Order deleted")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def search(request):
    customer = Customer.objects.get(id=request.GET["customer"])
    status = request.GET["status"]
    orders = Order.objects.filter(customer=customer, status=status)

    return render(request, "app/customer.html", {
            "customer": customer,
            "orders": orders,
            "status": STATUS,
        })



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "app/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return render(request, "app/register.html")
