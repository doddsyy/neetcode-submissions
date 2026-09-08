class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_visited = {}
        boxes = {}
        for row in range(len(board)):
            row_visited = set()
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    if board[row][col] in row_visited:
                        print('false due to row')
                        return False
                    row_visited.add(board[row][col])
                    if col in col_visited:
                        if board[row][col] in col_visited[col]:
                            print(col_visited)
                            print('false due to col')
                            return False
                        else:
                            col_visited[col].append(board[row][col])
                    else:
                        col_visited[col] = [board[row][col]]
                    boxr, boxc = row//3, col//3
                    if (boxr, boxc) in boxes:
                        if board[row][col] in boxes[(boxr, boxc)]:
                            print(boxes)
                            print('false bc of box')
                            print(board[row][col])
                            print(boxr)
                            print(boxc)
                            return False
                        else:
                            boxes[(boxr, boxc)].append(board[row][col])
                    else:
                        boxes[(boxr, boxc)] = [board[row][col]]
        return True
        


            
        