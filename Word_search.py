def word_search(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                # A recursive search here
                pointer = 0
                if search(i, j, board, word, pointer):
                    return True
    return False


def search(i, j, board, word, pointer):
    if pointer>=len(word):
        return True
    if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or word[pointer]!=board[i][j]:
        return False
    character = board[i][j]
    board[i][j] = "Visited"
    if search(i-1, j, board, word, pointer + 1):
        return True
    if search(i, j-1, board, word, pointer + 1):
        return True
    if search(i+1, j, board, word, pointer + 1):
        return True
    if search(i, j+1, board, word, pointer + 1):
        return True
    board[i][j] = character
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(word_search(board, word))