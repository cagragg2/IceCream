from django.shortcuts import render, render_to_response,redirect
from django.http import *
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from IceCreamVendingMachine.models import IceCream
from IceCreamVendingMachine.models import Stores
from IceCreamVendingMachine.models import WhereOffAmounts
from IceCreamVendingMachine.models import Users

# Create your views here.

def index(request):
	#users = Users.objects
	#context = { 'data': users }
	#username = password = ''
	#if request.POST:
	 #   username = request.POST['username']
	  #  password = request.POST['password']
	 #   user = authenticate(username=username, password=password)
  	 #   if user is not None:
		#login(request, user)
	#	return HttpResponseRedirect('/iceCreamList/')
	#return render_to_response('index.html', context_instance=RequestContext(request))
	return render( request, 'IceCreamVendingMachine/index.html')

#@login_required(login_url='/IceCreamVendingMachine/index')

#def login(request):
#	return render(request, 'IceCreamVendingMachine/index.html')
	
def main(request):
	ice_creams = WhereOffAmounts.objects.filter(stores = 6)
	IDs = IceCream.objects.filter(whereoffamounts__stores = 6)
	context = { 'data': zip(ice_creams, IDs) }
	return render(request, 'IceCreamVendingMachine/main.html', context)

def stores(request):
	storechosen = Stores.objects.order_by('storeName')
	context = { 'data': storechosen }
	return render(request, 'IceCreamVendingMachine/stores.html', context)

def select(request):
	return render(request, 'IceCreamVendingMachine/select.html')

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
	chosenIceCreamPrice = WhereOffAmounts.objects.filter(icecream = iceCreamID)
	context = { 'data': zip(chosenIceCream, chosenIceCreamPrice) }
	return render(request, 'IceCreamVendingMachine/receipt.html', context)
	
def storeAvailableList(request, storeID):
	all_items_in_store = IceCream.objects.filter(whereoffamounts__stores = storeID)
	store_chosen = Stores.objects.filter(storeID = storeID)
	amount_of_items = WhereOffAmounts.objects.filter(stores = storeID)
	context = { 'data' : zip(all_items_in_store, amount_of_items), 'store_chosen': store_chosen }
	return render(request, 'IceCreamVendingMachine/storeAvailableList.html',context)

def storeList(request, iceCreamID):
	current_Stores = Stores.objects.filter(whereoffamounts__icecream = iceCreamID)
	current_icecream = IceCream.objects.filter(iceCreamID = iceCreamID)
	context = { 'current_Stores': current_Stores, 'ID': iceCreamID, 'current_icecream': current_icecream }
	return render(request, 'IceCreamVendingMachine/storeList.html', context)
	
def successBuy(request, iceCreamID):
	chosen_ice_cream = iceCreamID
	context = { 'chosen_ice_cream': chosen_ice_cream }
	return render(request, 'IceCreamVendingMachine/successBuy.html', context)

def successLogin(request):
	return render(request, 'IceCreamVendingMachine/successLogin.html')


