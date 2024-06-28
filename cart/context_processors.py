from .cart import Cart

#Create context processors sp our can work on all pages
def cart(request):
    return {'cart':Cart(request)}