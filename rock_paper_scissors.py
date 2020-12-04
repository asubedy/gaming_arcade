import random
import time
 
"""
Working matrix of the game: 
            (0)Rock    (1)Paper   (2)Scissors    (3)Lizard  (4)Spock
(0)Rock         -1        1           0               0         4
 
(1)Paper         1       -1           2               3         1      
 
(2)Scissors      0        2          -1               2         4
 
(3)Lizard        0        3           2              -1         3           
 
(4)Spock         4        1           4               3        -1
 
Here -1 indicates a tie and all other positive numbers including 0 indicates the index of the winner of the tie. 
"""
import time
import random
class Game:
    name = ""
    results = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
    def __init__(self,user,comp):
        self.user = user
        self.comp = comp
    
    def displayWinner(self):
        who_won = Game.results[self.user][self.comp]
        if who_won == self.user:
            print(Game.name, "won the game!")
        elif who_won == self.comp:
            print("Computer won the game!")
        else:
            print("It was a tie.")


def random_number():
    return random.randint(0, 4)

def instructions_of_the_game():
    print()
    print("Instructions for Rock-Paper-Scissors-Lizard-Spock: ")
    print()
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()
    print("Scoring methodology: ",end="\n\n")
    print("WIN   : 1 point")
    print("LOOSE : 0 point ")
    print("TIE   : 1 point to each")
 
 
def random_number():
    return random.randint(0, 4)
 

def rock_paper_scissors_lizard_spock():
    a = True

    while a:
        print("\t\t\t\t\t\tWelcome to the Menu of the game!")
        print("If you need instructions on how to play the game please enter 'help'")
        print("If you want to start the game enter your choice: Rock, Paper, Scissor, Lizard, Spock")
        print("Enter exit to quit the game")
        print()
        
        choice = input("Enter your move: ")
        if choice.lower() == "help":
            instructions_of_the_game()
            continue
        elif choice.lower() == "rock":
            player_choice = 0
        elif choice.lower() == "paper":
            player_choice = 1
        elif choice.lower() == "scissors":
            player_choice = 2
        elif choice.lower() == "lizard":
            player_choice = 3
        elif choice.lower() == "spock":
            player_choice = 4
        elif choice.lower() == "exit":
            a = False
            print("Thank you for playing!")
            print("You will exit the game now!")
            break
        else:
            print("Error, wrong input!")
            continue
 
        print("It's the computer's turn now...")
        print("Wait while the computer makes its move")
        time.sleep(1)
        comp_choice = random_number()
        if comp_choice == 0:
            comp_move = "Rock"
        elif comp_choice == 1:
            comp_move = "Paper"
        elif comp_choice == 2:
            comp_move = "Scissors"
        elif comp_choice == 3:
            comp_move = "Lizard"
        else:
            comp_move = "Spock"
        print("Computer chose ", comp_move)
        time.sleep(2)
        #object of the class "Game called"
        player = Game(player_choice,comp_choice)
        player.displayWinner()
        # winner(player_choice, comp_choice)
        print("Game ended!")
        print()
        cont = input("Press y to continue and n to exit: ")
        if cont == 'n':
            print("Thank you for playing the game.")
            a = False

def start_game():
    A = True
    while A:
        Game.name = input("Enter Name")
        print("Let's Play Rock-Paper-Scissors-Lizard-Spock!")
        rock_paper_scissors_lizard_spock()
        print("Lets play again sometime.")
        A = False

#start_game()