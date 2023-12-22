def make_karnaugh_map(num_of_variables):
    if num_of_variables == 2:
        karnaugh_map = [[0, 1], [2, 3]]
    elif num_of_variables == 3:
        karnaugh_map = [[0, 1, 3, 2], [4, 5, 7, 6]]
    elif num_of_variables == 4:
        karnaugh_map = [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9, 11, 10]]
    else:
        print("이 함수는 2부터 4까지의 변수에 대한 카노맵을 지원합니다.")
        return None

    return karnaugh_map  

def display_karnaugh_map(karnaugh_map):
    for row in karnaugh_map:
        print(row)

def mark_boolean_function_positions(karnaugh_map, positions):
    for position in positions:
        for i in range(len(karnaugh_map)):
            if position in karnaugh_map[i]:
                j = karnaugh_map[i].index(position)
                karnaugh_map[i][j] = 'X'
    return karnaugh_map

def optimize_boolean_function(positions, num_of_variables): #일단 sop를 pos로 바꾸는걸 목표로 했음
    # 입력된 위치를 이진 문자열로 변환
    binary_strings = [format(pos, '0{}b'.format(num_of_variables)) for pos in positions]
    
    # 중복 제거를 위해 set으로 변환 후 리스트로 다시 변환
    unique_binary_strings = list(set(binary_strings))
    
    # 최적화된 부울 함수 (SOP 형태) 생성
    minimized_terms_sop = unique_binary_strings
    
    # SOP 형태의 항들을 POS 형태로 변환: 변환 과정에서 AB, AB'를 A가 아니라 두개의 항으로 표기하는 문제 있음
    pos_terms = get_pos_terms(minimized_terms_sop, num_of_variables)
    
    return minimized_terms_sop, pos_terms

def get_pos_terms(minimized_terms_sop, num_of_variables):
    # SOP 형태의 항들을 POS 형태로 변환
    pos_terms = []
    for sop_term in minimized_terms_sop:
        pos_term = ''
        for i, bit in enumerate(sop_term):
            if bit == '0':
                pos_term += f"{chr(ord('A') + i)}'"
            elif bit == '1':
                pos_term += f"{chr(ord('A') + i)}"
        pos_terms.append(pos_term)
    return pos_terms


num_of_variables = int(input("2부터 4까지의 변수의 개수를 입력해주세요: "))
karnaugh_map = make_karnaugh_map(num_of_variables)

if karnaugh_map:
    print("카르노 맵:")
    display_karnaugh_map(karnaugh_map)

    positions = list(map(int, input("부울 함수의 위치를 입력하세요 (공백으로 구분된 정수): ").split()))
    mark_boolean_function_positions(karnaugh_map, positions)

    print("부울 함수 표시된 카르노 맵:")
    display_karnaugh_map(karnaugh_map)

    # 부울 함수 최적화
    minimized_terms_sop, pos_terms = optimize_boolean_function(positions, num_of_variables)
    
    print("최적화된 부울 함수 (SOP):", minimized_terms_sop)
    print("최적화된 부울 함수 (POS):", pos_terms)









