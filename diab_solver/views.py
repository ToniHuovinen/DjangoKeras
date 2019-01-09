from django.shortcuts import render
from keras.models import load_model
from . import forms
from keras_model.diab_model import ProcessANN

loaded_model = load_model('./keras_model/diab.h5')
loaded_model._make_predict_function()


# Create your views here.
def index(request):

	form = forms.FormANN()

	model = ProcessANN(loaded_model)
	result = ""

	if request.method == 'POST':
		form = forms.FormANN(request.POST)

		if form.is_valid():

			# Fields from form cleaned
			a = form.cleaned_data['num_pregnant']
			b = form.cleaned_data['glucose_conc']
			c = form.cleaned_data['blood_pressure']
			d = form.cleaned_data['triceps']
			e = form.cleaned_data['insulin']
			f = form.cleaned_data['bmi']
			g = form.cleaned_data['pedigree']
			h = form.cleaned_data['age']

			returned_result = model.new_prediction(a,b,c,d,e,f,g,h)
			print(returned_result)
			result = str(returned_result)

	return render(request, 'diab_solver/index.html', {'form':form, 'result':result,})