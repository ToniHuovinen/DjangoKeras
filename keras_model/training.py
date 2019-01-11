"""
You only need to run this file when you want to retrain your model
This will save it in h5 format to this folder. That file then will be loaded in the django
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

# Loading the dataset with pandas
dataset = pd.read_csv("diabetes.csv")

# Using iloc to choose columns for the model
X = dataset.iloc[:, 0:8].values
y = dataset.iloc[:, 8].values

# Dataset has no categorical data that has any use for the model so we don't need any categorical encoding
# Splitting the dataset into training and validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


# Feature Scaling
scaler_X = StandardScaler()
X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

# Fitting the Logistic Regression and creating the Classifier
# Initialize ANN
classifier = Sequential()

# Add input layer and first hidden layer. Activation Function Relu and on output Sigmoid
classifier.add(Dense(units=12, kernel_initializer= 'uniform', activation= 'relu', input_dim=8))

# Add second hidden layer. Activation Function Relu 
classifier.add(Dense(units=8, kernel_initializer= 'uniform', activation= 'relu'))
classifier.add(Dropout(rate = 0.4))

# Add third hidden layer. Activation Function Relu 
classifier.add(Dense(units=6, kernel_initializer= 'uniform', activation= 'relu'))

# Output Layer
classifier.add(Dense(units=1, kernel_initializer= 'uniform', activation= 'sigmoid'))

# Compiling the ANN,
classifier.compile(optimizer= 'adam', loss= 'binary_crossentropy', metrics=['accuracy'])

# Fitting the ANN into the training set
fitted_model = classifier.fit(X_train, y_train, batch_size=10, epochs=30)

# Predictions
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)
y_modded = (y_test > 0.5)

# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_modded, y_pred)
print("Confusion Matrix")
print(cm)


classifier.save("diab.h5")
print("Model saved")


#############################
# TOOLS AND SUCH

# For checking out the max values of dataset
# Min values are 0
print("Max values in dataset:")
print(dataset.max())

# These are best run in Anaconda for example
# PLOTTING
# ACCURACY
#plt.plot(fitted_model.history['acc'])
#plt.plot(fitted_model.history['val_acc'])
#plt.title('Model Accuracy')
#plt.ylabel('accuracy')
#plt.xlabel('epoch')
#plt.legend(['train', 'test'], loc='upper left')
#plt.show()

# PLOTIING
# MODEL LOSS
#plt.plot(fitted_model.history['loss'])
#plt.plot(fitted_model.history['val_loss'])
#plt.title('Model Loss')
#plt.ylabel('Loss')
#plt.xlabel('Epoch')
#plt.legend(['train','test'], loc='upper right')
#plt.show()