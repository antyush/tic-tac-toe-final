# This is the main file

from logic import Game

# function to input a users move on the board
def input_move(board):
    x = int(input("Choose a row (1, 2, 3): "))
    y = int(input("Choose a column (1, 2, 3): "))
    if (x >= 1 or x <= 3) and (y >= 1 or y <= 3) and (board[x-1][y-1] == None):
        board[x - 1][y - 1] = new_game.player
        return(board)
    else:
        print("Try again. This coordinate out of bounds or already taken.")
        input_move(board)

if __name__ == '__main__':
    new_game = Game()

    # single or multi-player
    mode = input("How many players? [1 or 2]: ")

    # define the game mode
    new_game.game_type(mode) # user chooses X or O in logic


    while new_game.winner == None:
        if mode == '2': # multiplayer
            if new_game.player == 'X': # player 1's turn
                print('\nWe are taking a move from X')

                # player 1 makes a move
                input_move(new_game.board)
                new_game.winner = new_game.get_winner()

                # checking for winner
                if new_game.winner == new_game.player:
                    new_game.print_board()
                    print(new_game.player + " is the winner!")
                    break
            
            else: # player 2's turn
                print('\nWe are taking a move from O')

                # player 2 makes a move
                input_move(new_game.board)
                new_game.winner = new_game.get_winner()

                # checking for winner
                if new_game.winner == new_game.player:
                    new_game.print_board()
                    print(new_game.player + " is the winner!")
                    break
                
        else: # single player
            if new_game.player == 'X':
                new_game.bot = new_game.other_player(new_game.player)
                print('\nWe are taking a move from X')
                input_move(new_game.board)
                new_game.winner = new_game.get_winner()
                if new_game.winner == new_game.player:
                    new_game.print_board()
                    print(new_game.player + " is the winner!")
                    break
                print('\nWe are taking a move from O')
                new_game.bot_action()
                new_game.winner = new_game.get_winner()
                if new_game.winner == new_game.player:
                    new_game.print_board()
                    print(new_game.player + " is the winner!")
                    break
            else:
                new_game.bot = new_game.other_player(new_game.player)
                print('\nWe are taking a move from X')
                new_game.bot_action()
                new_game.winner = new_game.get_winner()
                if new_game.winner == new_game.player:
                    new_game.print_board()
                    print(new_game.player + " is the winner!")
                    break
                print('\nWe are taking a move from O')
                input_move(new_game.board)
                new_game.winner = new_game.get_winner()
                if new_game.winner == new_game.player:
                    new_game.print_board()
                    print(new_game.player + " is the winner!")
                    break

        print('\n Updated Board!')
        new_game.print_board()
            
        if mode == '2': # if multiplayer, switch player
            new_game.player = new_game.other_player(new_game.player)
            print("Now it is " + new_game.player + "'s turn!")