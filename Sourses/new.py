def make_karnaugh_map(num_of_variables):
    
    if num_of_variables == 2:
        karnaugh_map = [[0, 1], [2, 3]]
    elif num_of_variables == 3:
        karnaugh_map = [[0, 1, 3, 2], [4, 5, 7, 6]]
    elif num_of_variables == 4:
        karnaugh_map = [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9, 11, 10]]
        return karnaugh_map
    else:
        print("이 함수는 2부터 4까지의 변수에 대한 카노맵을 지원합니다.")

    return karnaugh_map  

def mark_boolean_function_positions(karnaugh_map, positions):
    for position in positions:
        for i in range(0,len(karnaugh_map)):
            if position in karnaugh_map[i]:
                j = karnaugh_map[i].index(position)
                karnaugh_map[i][j] = 'X'
    return karnaugh_map
    

num_of_variables = int(input("2부터 4까지의 변수의 개수를 입력해주세요: "))
karnaugh_map = make_karnaugh_map(num_of_variables)

if karnaugh_map:
    print("카르노 맵:")
    display_karnaugh_map(karnaugh_map)

    positions = list(map(int, input("부울 함수의 위치를 입력하세요 (공백으로 구분된 정수): ").split()))
    mark_boolean_function_positions(karnaugh_map, positions)

    print("부울 함수 표시된 카르노 맵:")
    display_karnaugh_map(karnaugh_map)
