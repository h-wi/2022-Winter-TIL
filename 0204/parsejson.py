import json


def reqToServer():
    file = 'C:/Users/bnmbn/OneDrive/Desktop/result.json'

    with open(file,'r') as f:
        prediction = json.load(f)

    res = prediction['predictions']
    # 2차원 리스트로 차원 낮추기
    result = sum(res,[])

    # [0.0091186082, 0.00606526947, 0.0375309959, 0.0488448329, 1.39943268e-05, 0.679534197, 0.168709919]
    # detection box x 좌표, y, box의 width, height, confidence, 클래스 1(can)에 대한 확률, 클래스 2(distorted)에 대한 확률
    # 이 데이터 한 덩어리가 리스트로 여러 개 존재함

    correct = []
    # confidence에 대해 임의의 threshold를 넘으면 그 데이터를 이 리스트에 넣는다.

    for i in range(len(result)):
        if (result[i][4] > 0.4): # threshold for confidence = 0.4
            correct.append(result[i])

    if (len(correct) == 0):
        return 'fail'

    for i in range(len(correct)):
        if (correct[i][5] > 0.8): # threshold for class probability (일단 can에 대한 확률로 해둠)
            return 'success'

    return 'fail'

print(reqToServer())