class KarnaughMap:
    def __init__(self, num_of_variables):
        self.map = self.make_karnaugh_map(num_of_variables)

    @staticmethod
    def make_karnaugh_map(num_of_variables):
        if num_of_variables == 2:
            return [[0, 1], [2, 3]]
        elif num_of_variables == 3:
            return [[0, 1, 3, 2], [4, 5, 7, 6]]
        elif num_of_variables == 4:
            return [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9, 11, 10]]
        else:
            print("이 함수는 2부터 4까지의 변수에 대한 카노맵을 지원합니다.")
            return None

    def display(self):
        for row in self.map:
            print(row)

    def mark_positions(self, positions):
        for position in positions:
            for i, row in enumerate(self.map):
                if position in row:
                    j = row.index(position)
                    self.map[i][j] = 'X'
        return self.map
