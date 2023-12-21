def make_karnaugh_map(num_of_variables):
    if num_of_variables > 4 or num_of_variables <= 1:
        print("이 함수는 2부터 4까지의 변수에 대한 카노맵을 지원합니다.")
    
    if num_of_variables == 4:
        karnaugh_map = [[0,1,3,2],[4,5,7,6],[12,13,15,14],[8,9,11,10]] 

    elif num_of_variables == 2:
        karnaugh_map = [[0,1],[2,3]]

    elif num_of_variables == 3:
        karnaugh_map = [[0,1,3,2],[4,5,7,6]]

        return  karnaugh_map

   
# 카노맵 생성 및 출력
num_of_variables = int(input(("2부터 4까지의 변수의 개수를 입력해주세요")))
karnaugh_map = make_karnaugh_map(num_of_variables)
for i in len(karnaugh_map):
    print(karnaugh_map[i])
