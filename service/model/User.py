import numpy as np
import operator
from service.model import Test_Process as TP
from service.model import ActivationFunction as AF


def MachineLearning(User_data,weight):
    v1 = np.dot(weight[0], User_data.reshape(49,-1))
    y1 = AF.Sigmoid(v1)
    
    v2 = np.dot(weight[1],y1)
    y2 = AF.Sigmoid(v2)

    v3 = np.dot(weight[2],y2)
    y3 = AF.ReLU(v3)

    v4 = np.dot(weight[3],y3)
    result= AF.Softmax(v4)
    result =list(result)

    Enterprinse_dictionary = {
                "삼성전자": result[0],
                "SK C&C": result[1],
                "대우중공업": result[2],
                "유니클로": result[3],
                "MBC": result[4],
                "에스체트": result[5],
                "한국전력공사": result[6],
                "루트로닉": result[7],
                "투니버스": result[8],
                "엑시콘": result[9],
            }
    sorted_value = sorted(Enterprinse_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    
    sorted_value = np.array(sorted_value)

    firstAccur = sorted_value[0][1]
    secondAccur = sorted_value[1][1]
    thirdAccur = sorted_value[2][1]
    Result_Dictionary = {
    "First" : sorted_value[0][0],
    "Second" : sorted_value[1][0],
    "Third" : sorted_value[2][0],

    "Accuracy_Fisrt" :  round(firstAccur[0] * 100, 3),
    "Accuracy_Second" : round(secondAccur[0] * 100, 3),
    "Accuracy_Third" : round(thirdAccur[0] * 100, 3),
    }

    # 기업변환을 위한 딕셔너리 생성
    # 결과값을 내림차순으로 정렬하여 관련도가 높은 상위 3개를 추천

    return Result_Dictionary

