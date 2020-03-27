# Django-username-validation-and-login  

## Check whether email exists or not  
```
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
```

## Data retrieval from the database once saved  
```
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
```


### Salient Features of this code  
<ol>
  <li> Contains code for posting the data into the database. </li>
  <li> Contains code for data rerieval from the database </li>
  <li> Check whether email exist or not and if exist will not enter such data again</li>
</ol>
  
### How to run this code  
To run this code, please install the requirements from requirements.txt file using the below command 
```
pip3 install requirements.txt
```
