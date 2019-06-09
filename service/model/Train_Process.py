import numpy as np
from service.model import ActivationFunction as AF
training_rate = 0.01
looping = 10

def Train_Process(w1,w2,w3,w4,X,D):
    for k in range(looping):
        Temp_X = np.array(X[k])
        x = Temp_X.reshape(49, -1)
        v1 = np.dot(w1 , x)
        y1 = AF.Sigmoid(v1)

        v2 = np.dot(w2 , y1)
        y2 = AF.Sigmoid(v2)

        v3 = np.dot(w3 , y2)
        y3 = AF.Sigmoid(v3)

        v = np.dot(w4 , y3)
        y = AF.ReLU(v)

        d = np.array(D[k])
        d = d.reshape(1,-1)
        e = np.subtract(d.T , y)       #기업의 correct answer
        
        delta = e

        e3= np.dot(w4.T,delta)
        delta3 = AF.ReLU_Prime(y3) * e3
        e2 = np.dot(w3.T,delta3)
        delta2 = AF.Sigmoid_Prime(y2) * e2
        e1 = np.dot(w2.T,delta2)
        delta1 = AF.Sigmoid_Prime(y1) * e1

        dw4 = training_rate * delta * y3.T
        w4 = w4 + dw4
        dw3 = training_rate * delta3 * y2.T
        w3 = w3 + dw3
        dw2 = training_rate * delta2 * y1.T
        w2 = w2 + dw2
        dw1 = training_rate * delta1 * x.T
        w1 = w1 + dw1

        weight = [w1,w2,w3,w4]
    return weight
