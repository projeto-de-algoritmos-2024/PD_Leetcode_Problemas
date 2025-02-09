from functools import lru_cache

class Solution:
    def slidingPuzzle(self, board):
        directions = [-1, 1, 3, -3]

        positions = [-1] * 6
        for i in range(2):
            for j in range(3):
                positions[board[i][j]] = i * 3 + j

        @lru_cache(None)
        def helper(moves, p0, p1, p2, p3, p4, p5):
            if (p0, p1, p2, p3, p4, p5) == (5, 0, 1, 2, 3, 4):
                return 0

            if moves <= 0:
                return float('inf')

            ans = float('inf')
            for d in directions:
                n0 = p0 + d
                cur_row, cur_col = divmod(p0, 3)
                new_row, new_col = divmod(n0, 3)

                if not (0 <= n0 < 6) or abs(cur_row - new_row) + abs(cur_col - new_col) != 1:
                    continue

                pos_list = [p0, p1, p2, p3, p4, p5]
                if n0 in pos_list[1:]:
                    idx = pos_list.index(n0)
                    pos_list[0], pos_list[idx] = pos_list[idx], pos_list[0]
                    ans = min(ans, 1 + helper(moves - 1, *pos_list))

            return ans

        result = helper(20, *positions)
        return result if result <= 20 else -1