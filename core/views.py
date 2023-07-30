from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from links.models import Link
from .forms import SignupForm
import razorpay
from saas.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
from .models import Donate


@login_required
def dashboard(request):
    newest_links = Link.objects.filter(created_by = request.user)
    return render(request, "core/dashboard.html", {"newest_links": newest_links})


@login_required
def Donatepage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        amount = int(request.POST.get('amount'))
        
        order_amount = 100 * amount
        order_currency ="INR"
        client = razorpay.Client(auth=( RAZORPAY_API_KEY , RAZORPAY_API_SECRET_KEY ))
        payment_order = client.order.create(dict(amount = order_amount, currency = order_currency, payment_capture = 1 ))
        payment_order_id = payment_order["id"]
        donar = Donate(name = name, number = number, amount = amount, order_id = payment_order_id)
        donar.save()
        context = { "amount" : amount, "number": number, "name": name, "api_key": RAZORPAY_API_KEY, "order_id": payment_order_id , }
        return render(request, 'core/donate.html', context)
        # return redirect('/')

    return render(request, "core/donate.html")


def index(request):
    name = request.user.username
    return render(request, 'core/index.html', {'name': name})


def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(username=user.username, password=user.password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

