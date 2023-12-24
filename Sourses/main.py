from KarnaughMap import KarnaughMap
from BooleanFunction import BooleanFunction

def main():
    num_vars = int(input("변수의 개수 (2, 3, 또는 4)를 입력하세요: "))
    minterms = input("부울 함수의 minterms를 공백으로 구분하여 입력하세요: ").split()

    k_map = KarnaughMap(num_vars)
    if k_map.map is not None:
        minterm_positions = [int(minterm) for minterm in minterms]
        marked_k_map = k_map.mark_positions(minterm_positions)
        k_map.display()

        print("SOP Simplification:", BooleanFunction.simplify_sop(marked_k_map))
        print("POS Simplification:", BooleanFunction.simplify_pos(marked_k_map))

if __name__ == "__main__":
    main()








