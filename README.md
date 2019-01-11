# DjangoKeras (wip)

With this project I am trying to learn more about Django itself and Keras deep learning models. For deep learning part, I have created a simple binary classification model with Pima Indians diabetes data. Data itself is public and widely used and this particular set is from Kaggle and contains these features:

* Pregnancies, Number of times pregnant
* Glucose, Plasma glucose concentration a 2 hours in an oral glucose tolerance test
* BloodPressure, Diastolic blood pressure (mm Hg)
* SkinThickness, Triceps skin fold thickness (mm)
* Insulin, 2-Hour serum insulin (mu U/ml)
* BMI, Body mass index (weight in kg/(height in m)^2)
* DiabetesPedigreeFunction
* Age, years
* Outcome (1 or 0, True or False)


![Accuracy and model loss](https://github.com/ToniHuovinen/DjangoKeras/blob/master/git_images/charts.png)


You can install all the dependencies with the supplied requirements.txt file


Accuracy of the Keras deep learning model is around 80%. I have included a training.py script for retraining of the model. The way this project works is that when you start the local server with command 'python manage.py runserver', you will first set up the Tensorflow backend, and after that server starts and model is loaded once.


After that you can go to address localhost:8000 to see the webpage. There you can insert your values to the fields and upon pressing the submit button, you will get a result back. 


At this moment page is not responsive at all. That is next on my list. Will also add validation and rangelimits on the fields. 
