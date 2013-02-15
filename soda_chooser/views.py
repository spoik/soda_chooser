# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from soda_chooser.models import Beverage

def index(request):
	beverage = Beverage.objects.order_by('?')
	if len(beverage) == 0:
		beverage = None
	else:
		beverage = beverage[0]

	return render_to_response(
		'index.html',
		{
			'beverage': beverage
		}
	)

def would_drink(request, beverage_id):
	beverage = get_object_or_404(Beverage, pk=beverage_id)
	beverage.would_drink = beverage.would_drink + 1
	beverage.save()
	return redirect('index')

def would_not_drink(request, beverage_id):
	beverage = get_object_or_404(Beverage, pk=beverage_id)
	beverage.would_not_drink = beverage.would_not_drink + 1
	beverage.save()
	return redirect('index')
