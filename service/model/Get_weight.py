import numpy as np

First_row = 55*49
Second_row = 50*55
Third_row = 50*50
Fourth_row = 10*50

null_w1,null_w2,null_w3,null_w4,weight=[],[],[],[],[]

for i in range(First_row):
    null_w1.append(2*np.random.random()-1)
Temp_w1 = np.array(null_w1)
w1 = Temp_w1.reshape(55,-1)

for i in range(Second_row):
    null_w2.append(2*np.random.random()-1)
Temp_w2 = np.array(null_w2)
w2 = Temp_w2.reshape(50,-1)

for i in range(Third_row):
    null_w3.append(2*np.random.random()-1)
Temp_w3 = np.array(null_w3)
w3 = Temp_w3.reshape(50,-1)

for i in range(Fourth_row):
    null_w4.append(2*np.random.random()-1)
Temp_w4 = np.array(null_w4)
w4 = Temp_w4.reshape(10,-1)

weight.append(w1)
weight.append(w2)
weight.append(w3)
weight.append(w4)



