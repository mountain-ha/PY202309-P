class BooleanFunction:
    @staticmethod
    def simplify_sop(karnaugh_map):
        rows = len(karnaugh_map)
        cols = len(karnaugh_map[0])
        simplified_terms = []

        for i in range(rows):
            for j in range(cols):
                if karnaugh_map[i][j] == 'X':
                    term = []
                    if rows == 4:
                        term.append('A' if i < 2 else 'A\'')
                    if rows >= 2:
                        term.append('B' if i % 2 == 0 else 'B\'')
                    if cols == 4:
                        term.append('C' if j < 2 else 'C\'')
                    if cols >= 2:
                        term.append('D' if j % 2 == 0 else 'D\'')
                    simplified_terms.append(''.join(term))

        return ' + '.join(simplified_terms)

    @staticmethod
    def simplify_pos(karnaugh_map):
        rows = len(karnaugh_map)
        cols = len(karnaugh_map[0])
        simplified_terms = []

        for i in range(rows):
            for j in range(cols):
                if karnaugh_map[i][j] != 'X':
                    term = []
                    if rows == 4:
                        term.append('A' if i >= 2 else 'A\'')
                    if rows >= 2:
                        term.append('B' if i % 2 != 0 else 'B\'')
                    if cols == 4:
                        term.append('C' if j >= 2 else 'C\'')
                    if cols >= 2:
                        term.append('D' if j % 2 != 0 else 'D\'')
                    simplified_terms.append('(' + ' + '.join(term) + ')')

        return ' * '.join(simplified_terms)
