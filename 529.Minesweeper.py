class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        def nearly_bombs(row, col, rows, cols):
            n = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if not (i == j == 0) and 0 <= row + i < rows and 0 <= col + j < cols:
                        n += board[row + i][col + j] == 'M'
            return n


        stack = [click]
        while len(stack):
            x, y = stack.pop()
            if board[x][y] == 'E':
                n = nearly_bombs(x,y,len(board), len(board[0]))
                if n == 0:
                    board[x][y] = 'B'
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if not (i == j == 0) and 0 <= x+i < len(board) and 0 <= y+j < len(board[0]):
                                stack.append([x+i, y+j])                    
                else:
                    board[x][y] = str(n)

        return board
