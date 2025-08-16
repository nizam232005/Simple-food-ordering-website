from django.shortcuts import render,HttpResponse,redirect
from .import models


def index(request):
    return render(request, 'index.html')
# Create your views here.
def registration(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        address = request.POST.get('address')
        if models.reg.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        else:
            user = models.reg(name=name, age=age,gender=gender, email=email, password=password, image=image, address=address)
            user.save()
            return redirect('index')
    return render(request, 'registration.html')
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = models.reg.objects.get(email=email)
            if user.password == password:
                request.session['email'] = email
                return redirect('home')
            else:
                return HttpResponse("Invalid credentials")
        except models.reg.DoesNotExist:
            return HttpResponse("Invalid email or password")
    return render(request, 'login.html')


def profile(request):
    if 'email' in request.session:
        email = request.session['email']
        try:
            client = models.reg.objects.get(email=email)
            
            return render(request, 'profile.html', {'c': client})
        except models.reg.DoesNotExist:
            return HttpResponse("User not found")
    else:
        return HttpResponse("not logged in")


def editprofile(request):
    if 'email' in request.session:
        email = request.session['email']
        try:
            client = models.reg.objects.get(email=email)
            if request.method == 'POST':
                client.name = request.POST.get('name')
                client.age = request.POST.get('age')
                client.gender = request.POST.get('gender')
                client.email = request.POST.get('email')
                client.address = request.POST.get('address')
                client.image = request.FILES.get('image')
                client.password = request.POST.get('password')
                client.phone = request.POST.get('phone')
                client.save()
                return redirect('profile')
            return render(request, 'editprofile.html', {'c': client})
        except models.reg.DoesNotExist:
            return HttpResponse("User not found")
    else:
        return HttpResponse("user not found")
    

def home(request):
    return render(request, 'home.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        adminusername = 'ADMIN'
        adminpassword = 'admin'
        if username == adminusername: 
            if  password == adminpassword:
                return redirect('adminhome')
            else:
                return redirect('adminlogin')
        else:
            return redirect('adminlogin')
    return render(request, 'adminlogin.html')

def logout(request):
    if 'email' in request.session:
        request.session.flush()
        return redirect('index')
    else:
        return redirect('index')
    
def adminhome(request):
    return render(request,'adminhome.html')

def addproduct(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        # quantity is now included in the form
        quantity = request.POST.get('quantity')  # Assuming quantity is a field in the form
        image = request.FILES.get('image')
        description = request.POST.get('description')
        status = request.POST.get('status')
        product = models.product(name=name, price=price, image=image, description=description, status=status)
        product.save()
        return redirect('productlist')
    return render(request, 'addproduct.html')

def productlist(request):
    item=models.product.objects.all()
    return render(request,'productlist.html',{'c': item})


def editproduct(request, id):
    item = models.product.objects.get(id=id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.description = request.POST.get('description')
        item.status = request.POST.get('status')

        image = request.FILES.get('image')
        if image:  # Only replace image if new one uploaded
            item.image = image

        item.save()  # Always save changes
        return redirect('productlist')

    return render(request, 'editproduct.html', {'product': item})



def deleteproduct(request, id):
    item = models.product.objects.filter(id=id)
    item.delete()
    return redirect('productlist')


def userlist(request):
    users = models.reg.objects.all()
    return render(request, 'userlist.html', {'users': users})
    

def userproductlist(request):
    products = models.product.objects.all()
    return render(request, 'userproductlist.html', {'products': products})


def addtocart(request, pdid):
    if 'email' in request.session:
        email = request.session['email']
        user = models.reg.objects.get(email=email)
        product = models.product.objects.get(id=pdid)
        
        if request.method == 'POST':
            quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not specified
            totalprice = product.price * quantity
            
            cart_item, created = models.cart.objects.get_or_create(
                user=user,
                product=product,
                defaults={'quantity': quantity, 'totalprice': totalprice}
            )
            
            if not created:  # If the item already exists, update it
                cart_item.quantity += quantity
                cart_item.totalprice += totalprice
                cart_item.save()
            
            return redirect('userproductlist')
             
    else:
        return HttpResponse("You need to log in to add items to the cart.")
    
    return redirect('login')

def usercartlist(request):
    if 'email' in request.session:
        user_email = request.session['email']
        user = models.reg.objects.get(email=user_email)
        cart_items = models.cart.objects.filter(user=user)
        
        return render(request, 'usercartlist.html', {'cart_items': cart_items})
    else:
        return redirect('login')
    


def admincartlist(request):
    if 'email' in request.session:
        user_email = request.session['email']
        user = models.reg.objects.get(email=user_email)
        cartitems = models.cart.objects.filter(user=user)
        
        return render(request, 'admincartlist.html', {'cartitems': cartitems})
    else:
        return redirect('adminlogin')




def favourites(request):
    
    if 'email' in request.session:
        user_email = request.session['email']
        user = models.reg.objects.get(email=user_email)
        favouriteitems = models.favourite.objects.filter(user=user)
        
        return render(request, 'favourites.html', {'favouriteitems': favouriteitems})
    else:
        return redirect('login')
    

def addtofavourites(request, pdid):
    if 'email' in request.session:
        user_email = request.session['email']
        user = models.reg.objects.get(email=user_email)
        product = models.product.objects.get(id=pdid)
        
        # Check if the product is already in favourites
        favourite_item, created = models.favourite.objects.get_or_create(
            user=user,
            product=product
        )
        
        if created:
            return HttpResponse("Product added to favourites.")
        else:
            return HttpResponse("Product is already in favourites.")
    else:
        return redirect('login')