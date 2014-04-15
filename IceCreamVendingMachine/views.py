from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from IceCreamVendingMachine.models import IceCream
from IceCreamVendingMachine.models import Stores

# Create your views here.

def index(request):
	all_icecreams = IceCream.objects.order_by('-flavor')
	template = loader.get_template('IceCreamVendingMachine/index.html')
	context = RequestContext(request, { 'all_icecreams': all_icecreams,})
	return HttpResponse(template.render(context))

#def detail(request, iceCreamID):
#    return HttpResponse("You're looking at poll %s." % iceCreamID)

def login(request):
	return render(request, 'IceCreamVendingMachine/index.html')
	
def failureBuy(request):
	return render(request, 'IceCreamVendingMachine/failureBuy.html')

def failureLogin(request):
	return render(request, 'IceCreamVendingMachine/failureLogin.html')

def iceCreamList(request):
	all_icecreams = IceCream.objects.order_by('-flavor')
	context = { 'all_icecreams': all_icecreams}
	return render(request, 'IceCreamVendingMachine/iceCreamList.html', context)

def receipt(request, iceCreamID):
	chosenIceCream = IceCream.objects.filter(iceCreamID = iceCreamID)
	context = { 'chosenIceCream': chosenIceCream }
	return render(request, 'IceCreamVendingMachine/receipt.html', context)
	
def storeAvailableList(request, iceCreamID):
	all_items_in_store = IceCream.objects.filter(whereoff__stores = iceCreamID)
	context = { 'all_items_in_store': all_items_in_store }
	return render(request, 'IceCreamVendingMachine/storeAvailableList.html',context)

def storeList(request, iceCreamID):
	current_Stores = Stores.objects.filter(whereoff__icecream = iceCreamID)
	context = { 'current_Stores': current_Stores }
	return render(request, 'IceCreamVendingMachine/storeList.html', context)
	
def successBuy(request, iceCreamID):
	chosen_ice_cream = iceCreamID
	context = { 'chosen_ice_cream': chosen_ice_cream }
	return render(request, 'IceCreamVendingMachine/successBuy.html', context)

def successLogin(request):
	return render(request, 'IceCreamVendingMachine/successLogin.html')


