class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for move in moves.upper():
            x, y = (x + 1, y) if move == 'R' else (x - 1, y) if move == 'L' \
                else (x, y + 1) if move == 'D' else (x, y - 1) if move == 'U' \
                else (x, y)

        return x == 0 and y == 0