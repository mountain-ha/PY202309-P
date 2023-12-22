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
        for i, row in enumerate(karnaugh_map):
            if position in row:
                j = row.index(position)
                karnaugh_map[i][j] = 'X'
    return karnaugh_map

def optimize_boolean_function(positions, num_of_variables):
    # 입력된 위치를 이진 문자열로 변환
    binary_strings = [format(pos, '0{}b'.format(num_of_variables)) for pos in positions]

    # 최적화된 부울 함수 (SOP 형태) 생성
    minimized_terms_sop = list(set(binary_strings))

    # SOP 형태의 항들을 POS 형태로 변환
    pos_terms = get_pos_terms(minimized_terms_sop)

    return minimized_terms_sop, pos_terms

def get_pos_terms(minimized_terms_sop):
    # SOP 형태의 항들을 POS 형태로 변환
    pos_terms = [''.join([f"{chr(ord('A') + i)}'" if bit == '0' else f"{chr(ord('A') + i)}" for i, bit in enumerate(term)]) for term in minimized_terms_sop]
    return pos_terms

def simplify_pos_terms(pos_terms):
    grouped_terms = {}
    for term in pos_terms:
        key = ''.join(sorted(term))
        grouped_terms.setdefault(key, []).append(term)

    simplified_terms = []
    for key, terms in grouped_terms.items():
        if len(terms) == 1:
            simplified_terms.append(terms[0])
        else:
            common_factors = ''.join([c for c in key if key.count(c) == len(terms)])
            additional_factors = ''.join([c for c in key if key.count(c) < len(terms)])
            simplified_terms.append(f"({common_factors}+{additional_factors}')")

    return simplified_terms

# 메인 코드
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
    print("최적화된 부울 함수 (POS):", get_pos_terms(minimized_terms_sop))









