#Define terminal function (Asseses wheter or not the game is over)
def terminal(board):
    for  i in range(3):
        if board[i][0]==board[i][1]==board[i][2] != '' or board[0][i]==board[1][i]==board[2][i] !='':
            return True
        
    if board[0][0]==board[1][1]==board[2][2] !='' or board[0][2]==board[1][1]==board[2][0] != '':
        return True
    
    for row in board:
        if any(element == '' for element in row):
            return False

    return True

#Define score function (Assigns a score of 1 if AI wins, 0 if it's a draw, -1 if player wins)
def score(board):
    for row in board:
        if all(cell == 'X' for cell in row):
            return 1
        elif all(cell == 'O' for cell in row):
            return -1

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 1
        elif all(board[row][col] == 'O' for row in range(3)):
            return -1

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return -1

    return 0

#Define actions function (Returns possible moves on the board)
def actions(board):
    moves=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                moves.append((i,j))
    return moves

#Define minimax algorithm (AI learning algorithm)
def minimax(board, depth, maximizing_player):
    if terminal(board):
        return score(board)
    
    if maximizing_player:
        max_score = float('-inf')
        for action in actions(board):
            board[action[0]][action[1]] = 'X'
            value=minimax(board,depth+1,False)
            board[action[0]][action[1]]=''
            max_score=max(max_score,value)
        return max_score
    else:
        min_score = float('inf')
        for action in actions(board):
            board[action[0]][action[1]] = 'O'
            value=minimax(board,depth+1,True)
            board[action[0]][action[1]]=''
            min_score=min(min_score,value)
        return min_score

#Define best action function (Returns the best move on the board for the AI)
def best_action(board):
    if terminal(board):
        return score(board)
    max_score = float('-inf')
    best_move = None
    for action in actions(board):
      board[action[0]][action[1]]='X'
      value = minimax(board,0,False)
      board[action[0]][action[1]]=''
      if value > max_score : 
          max_score = value
          best_move = action
    return best_move

#Define play the game function (You play the game against the AI)
def play_the_game(board):
    while not(terminal(board)):
        AI_move =best_action(board)
        board[AI_move[0]][AI_move[1]] = 'X'
        if not(terminal(board)):
            print_tic_tac_toe_board(board)
            Players_move = input('Input a move:')
            Players_move = int(Players_move)
            board[Players_move // 10][Players_move % 10] = 'O'
        else:
            if score(board) == 1:
                return (print_tic_tac_toe_board(board))
            elif score(board) == 0:
                return (print_tic_tac_toe_board(board))
            else:
                return (print_tic_tac_toe_board(board))
    if score(board) == 1:
        return (print_tic_tac_toe_board(board))
    elif score(board) == 0:
        return (print_tic_tac_toe_board(board))
    else:
        return (print_tic_tac_toe_board(board))
    
#Define a simple graphic representation of the board
def print_tic_tac_toe_board(board):
    for row in board:
        print(' | '.join(cell if cell != '' else ' ' for cell in row))
        print('-' * 9)

#Define the starting board 
board=[
    ['','',''],
    ['','O',''],
    ['','','']
    ]

#Play the game!
play_the_game(board)