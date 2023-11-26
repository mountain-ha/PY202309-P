import pandas as pd
import itertools

def generate_gray_code(n):
    """
    n 비트에 대한 그레이 코드를 생성합니다.
    """
    gray_code = []
    for i in range(2 ** n):
        gray_code.append((i >> 1) ^ i)
    return gray_code

def draw_karnaugh_map(variables):
    """
    주어진 변수의 개수에 대한 카르노 맵을 그립니다.
    """
    n = 2 ** variables
    gray_code = generate_gray_code(variables)

    # 카르노 맵을 나타내는 DataFrame 생성
    karnaugh_map = pd.DataFrame(index=range(n), columns=range(variables))

    # 각 칸에 해당하는 값 적기
    for i in range(n):
        for j in range(variables):
            karnaugh_map.at[i, j] = gray_code[i] % 2
            gray_code[i] //= 2

    print("카르노 맵:")
    print(karnaugh_map)

    # 각 칸의 숫자와 이진수를 매핑하는 딕셔너리 생성
    mapping_dict = {}
    for i in range(n):
        binary_value = ''.join(map(str, karnaugh_map.iloc[i].tolist()))
        mapping_dict[i] = binary_value

    print("\n카르노 맵 숫자와 이진수 매핑:")
    print(mapping_dict)

# 사용자로부터 변수의 개수를 입력으로 받기
num_variables = int(input("변수의 개수를 입력하세요 (2에서 4까지): "))

if num_variables < 2 or num_variables > 4:
    print("변수의 개수는 2에서 4까지의 값이어야 합니다.")
else:
    draw_karnaugh_map(num_variables)






