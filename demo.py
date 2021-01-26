a=[ 0.00632 , 18.00 ,  2.310 , 0 , 0.5380 , 6.5750 , 65.20 , 4.0900  , 1 , 296.0 , 15.30, 396.90  , 4.98]
price=24.00
import numpy as np
from numpy.core.records import array
array_data =np.array(a)
from joblib import dump, load
model = load('VC_Awsome.joblib')
data = array_data.reshape(1,13)
print(data)
results = model.predict(data)
print(results)