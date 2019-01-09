from django import forms


class FormANN(forms.Form):

	num_pregnant = forms.FloatField()
	glucose_conc = forms.FloatField()
	blood_pressure = forms.FloatField()
	triceps = forms.FloatField()
	insulin = forms.FloatField()
	bmi = forms.FloatField()
	pedigree = forms.FloatField()
	age = forms.IntegerField()