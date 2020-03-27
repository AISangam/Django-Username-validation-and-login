from django.shortcuts import render
from .models import Registeration
# Create your views here.

""" Function to save data into database
	Remember POST is used to save data in database
	Whereas GET is used to retrieve data from database
"""	

def form_validation(request):
	if request.method == "POST":
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('psw')
		registeration = Registeration()
		registeration.username = username
		registeration.email = email
		registeration.password = password
		try:
			object_from_db = Registeration.objects.get(password=password)
			email_verification = object_from_db.email
			if email_verification == email:
				return render(request, 'already_taken.html')
			else:
				registeration.save()
				return render(request, 'data_saved.html')		
		except:
			registeration.save()
			return render(request, 'data_saved.html')
	
	return render(request, 'registeration.html')	

""" Function to get all data from the database """	
def get_data_from_db(request):
	query_set = Registeration.objects.all()
	dict_values = dict()
	for each_value in query_set:
		name = each_value.username
		email = each_value.email
		password = each_value.password
		dict_values.setdefault('name', [])
		dict_values.setdefault('email', [])
		dict_values.setdefault('password', [])
		dict_values['name'].append(name)
		dict_values['email'].append(email)
		dict_values['password'].append(password)
	return render(request, 'get_data.html', {'context':dict_values})	