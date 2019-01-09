
import numpy as np
from sklearn.preprocessing import StandardScaler


class ProcessANN():

	def __init__(self, model):
		self.model = model

	def new_prediction(self, a, b, c, d, e, f, g, h):
		sc = StandardScaler()

		arr = np.array([[a,b,c,d,e,f,g,h]])

		# Do some reshaping and fitting using StandardScaler
		arr = np.reshape(arr, (8,1))
		arr = sc.fit_transform(arr)
		arr = np.reshape(arr, (1,8))

		# New prediction
		new_prediction = self.model.predict(arr)
		new_prediction = (new_prediction > 0.5)

		return new_prediction[0][0]