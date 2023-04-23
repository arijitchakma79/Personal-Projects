import random
class TicTacToe:
    def __init__(self):
        self.board=[" " for x in range(9)] #It will give a list of [" "," "," "," "," "," "," "," "," "]
        self.player1="X"
        self.player2="O"
        self.current_player=self.player1    
        self.winner=None
        self.computer_player=False
        

    #Displaying the 2-D Array. 
    def display_board(self):
        for x in range(3):
            print(f"| {self.board[x*3]} | {self.board[(x*3)+1]} | {self.board[(x*3)+2]} |")
            print("---------------")

    #The above code will print something like the following:
#     |   |   |   |
#   ----------------
#     |   |   |   |
#   ----------------
#     |   |   |   |
#   ----------------
    #Checks if the board is filled or not.
    def is_board_filled(self):
        if " " in self.board:  #if there is even a single " " in board, then the board is not filled and there are space left to play. 
            return False
        return True
    
    def is_winner(self,player):
        #Checks the rows:
        for x in range(3):
            if self.board[x*3]==self.board[(x*3)+1]==self.board[(x*3)+2]==player:
                return True
        
        #Checks the columns:
        for x in range(3):
            if self.board[x]==self.board[x+3]==self.board[x+6]==player:
                return True
        
        #Checks the diagonals:
        if self.board[0]==self.board[4]==self.board[8]==player: #Top left to bottom right diagonal
            return True
        if self.board[2]==self.board[4]==self.board[6]==player: #Top right to bottom left diagonal
            return True

        return False  #if nothing matches then it returns False
    
    def check_tie(self):
        if self.is_board_filled() and not self.is_winner(self.current_player):
            return True
        return False
    
    def available_moves(self):
        moves=[]
        for x in range(9):
            if self.board[x]==" ":
                moves.append(x)
        return moves
    

    def make_move(self,position):
        if self.board[position]==" ":
            self.board[position]=self.current_player
            return True
        return False
    
    def change_player(self):
        if self.current_player==self.player1:
            self.current_player=self.player2
        else:
            self.current_player=self.player1

    def display_board_numbers(self):
        for x in range(3):
            print(f"| {x*3} | {(x*3)+1} | {(x*3)+2} |")
            print("---------------")
    
    
    def minimax(self,board,depth,maximizing_player,minimizing_player):
        if self.is_winner(maximizing_player):
            return 1
        if self.is_winner(minimizing_player):
            return -1
        if self.is_board_filled():
            return 0
        
        if maximizing_player:
            best_score=-10000
            for move in self.available_moves():
                board[move]=maximizing_player
                score=self.minimax(board,depth+1,False,minimizing_player)
                board[move]=" "
                best_score=max(score,best_score)
            return best_score
        else:
            best_score=10000
            for move in self.available_moves():
                board[move]=minimizing_player
                score=self.minimax(board,depth+1,True,maximizing_player)
                board[move]=" "
                best_score=min(score,best_score)
            return best_score
        
    def get_best_move(self):
        best_score=-10000
        best_move=0
        for move in self.available_moves():
            self.board[move]=self.current_player
            score=self.minimax(self.board,0,False,self.current_player)
            self.board[move]=" "
            if score>best_score:
                best_score=score
                best_move=move
        return best_move
    
    def random_start(self):
        if random.randint(0,1)==0:
            self.current_player=self.player2
        else:
            self.current_player=self.player1
    
    
    
    def play_against_computer(self):
        print("Welcome to my Command Line Version of Tic-Tac-Toe\n")
        print("The board is numbered as follows:\n")
        self.random_start()
        while True:
            self.display_board_numbers()
            print(" ")
            if self.current_player==self.player1:
                print(f"Player {self.current_player}'s turn\n")
            else:
                print(f"Computer's turn\n")
            self.display_board()
            print(" ")
            if self.current_player==self.player1:
                try:
                    position=int(input("Enter a position (0-8): "))
                    print(" ")
                    if position<0 or position>8:
                        print("Position out of range")
                    else:
                        if self.make_move(position):
                            if self.is_winner(self.current_player):
                                self.winner=self.current_player
                                break
                            if self.check_tie():
                                break
                            self.change_player()
                        else:
                            print("Invalid move! Position Already Taken.")
                            print(" ")
                        print("")
                except ValueError:
                    print("Invalid input! Please enter a number between 0-8")
                    print(" ")
            else:
                position=self.get_best_move()
                if self.make_move(position):
                    if self.is_winner(self.current_player):
                        self.winner=self.current_player
                        break
                    if self.check_tie():
                        break
                    self.change_player()
                else:
                    print("Invalid move! Position Already Taken.")
                    print(" ")
                print("")

        self.display_board()

        if self.winner==self.player1:
            print(f"Player {self.player1} wins!")
        elif self.winner==self.player2:
            print(f"Computer wins!")
        else:   
            print("Tie game!")

        while True:
            play_again=input("Want to play again? (y/n): ").lower()
            if play_again=="y":
                self.__init__()
                self.play_against_computer()
           
            elif play_again=="n":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input.")


    def play_game(self):
        self.__init__()
        play_computer=input("Do you want to play against the computer? (y/n): ").lower()
        if play_computer=="y":
            self.play_against_computer()
        else:

            print("Welcome to my Command Line Version of Tic-Tac-Toe\n")
            print("The board is numbered as follows:\n")
            
            while True:
                self.display_board_numbers()
                print(" ")
                print(f"Player {self.current_player}'s turn\n")
                self.display_board()
                print(" ")
                try:
                    position=int(input("Enter a position (0-8): "))
                    print(" ")
                    if position<0 or position>8:
                        print("Position out of range")
                    else:
                        if self.make_move(position):
                            if self.is_winner(self.current_player):
                                self.winner=self.current_player
                                break
                            if self.check_tie():
                                break
                            self.change_player()
                        else:
                            print("Invalid move! Position Already Taken.")
                            print(" ")
                        print("")
                except ValueError:
                    print("Invalid input! Please enter a number between 0-8")
                    print(" ")
            
            self.display_board()

            if self.winner==self.player1:
                print(f"Player {self.player1} wins!")
            elif self.winner==self.player2:
                print(f"Player {self.player2} wins!")
            else:   
                print("Tie game!")

            while True:
                play_again=input("Want to play again? (y/n): ").lower()
                if play_again=="y":
                    self.__init__()
                    self.play_game()
            
                elif play_again=="n":
                    print("Thanks for playing!")
                    break
                else:
                    print("Invalid input.")

    
#just a random change.
if __name__=="__main__":
    game=TicTacToe()
    game.play_game()





    

    




    



