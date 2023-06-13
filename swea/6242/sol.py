blood  = {
    'A' : 0,
    'B' : 0,
    'O' : 0,
    'AB' : 0,
}

blood_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

for blood_test in blood_list:
    blood[blood_test] += 1

# 두번째 방법

location = ['서울', '대전', '대구','부산']
location_dict = {}

for l in location:
    # 이미 기록한 경우
    if l in location_dict.keys():
        location_dict[l] += 1
    # 처음으로 등장한 경우
    else: 
        location_dict[l] = 1

print(location_dict)