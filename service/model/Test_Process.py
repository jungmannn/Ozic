from service.model import Train_Process
from service.model import Get_weight as Weight
from service.model import Database
# Training 횟수 정의
# X = 기업에서 입력한 CORRECT한 데이터
# D = Training을 위한 label 데이터

def Test_Processing():
    weight = Train_Process.Train_Process(Weight.w1, Weight.w2, Weight.w3, Weight.w4, Database.X, Database.D)
    Epoch = 50000
    for i in range(Epoch):

        w1 = weight[0]
        w2 = weight[1]
        w3 = weight[2]
        w4 = weight[3]

        weight = Train_Process.Train_Process(w1, w2, w3, w4, Database.X, Database.D)

    return weight
