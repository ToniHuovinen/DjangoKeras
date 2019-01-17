from django import forms


class FormANN(forms.Form):

	num_pregnant = forms.FloatField(label="No. pregnacies (0 - 20)")
	glucose_conc = forms.FloatField(label="Glucose (0 - 200)")
	blood_pressure = forms.FloatField(label="Blood pressure (0 - 130)")
	triceps = forms.FloatField(label="Skin thickness (0 - 100)")
	insulin = forms.FloatField(label="Insulin (0 - 900)")
	bmi = forms.FloatField(label="BMI (0 - 70)")
	pedigree = forms.FloatField(label="Diabetes ped function (0 - 3)")
	age = forms.IntegerField(label="Age (0 - 90)")