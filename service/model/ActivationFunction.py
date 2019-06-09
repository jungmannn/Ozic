import numpy as np

#각 Layer를 지날때에 activation function을 정의

def Sigmoid(x):
    return 1 / (1 + np.exp(-x))
def ReLU(x):
    return np.maximum(0,x)
def Softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    y = exp_x / ( sum_exp_x)
    return y
def ReLU_Prime(x):
    return np.where(x>0, 1.0, 0.0)
def Sigmoid_Prime(x):
   return Sigmoid(x)/(1-Sigmoid(x))

