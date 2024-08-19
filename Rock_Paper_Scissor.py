
import random


print("Welcome to Rock Paper Scissors!")
print("-------------------------------")

# setup variables 

CPU_score = 0
player_score = 0 
tie_score = 0 
Possible_Hands = ["Rock","Paper","Scissors"]


def checkForWinner(playerHand,computerHand):
    
    if(playerHand == "Rock" and computerHand == "Paper"):
        print("Sorry You Lost :(")
        return "CPU"
        
    elif(playerHand == "Rock" and computerHand == "Scissors"):
        print("Congrats! You Have Won :)")
        return "Player"
    
    elif(playerHand == "Scissors" and computerHand == "Paper"):
        print("Congrats! You Have Won :)")
        return "Player"
    
    elif(playerHand == "Scissors" and computerHand == "Rock"):
        print("Sorry You Lost :(")
        return "CPU"
    
    elif(playerHand == "Paper" and computerHand == "Rock"):
        print("Congrats! You Have Won :)")
        return "Player"
    
    elif(playerHand == "Paper" and computerHand == "Scissors"):
        print("Sorry You Lost :(")
        return "CPU"
    
    else:
        print("It's a Tie , Play Again!")
        return "Tie"
    
    
    # start game Loop
while (player_score != 3 and CPU_score != 3):
    # validate input
    while True:
            playerHand = input("\n Pick a hand. Rock,Paper or Scissors: ")

            if(playerHand == "Rock" or playerHand == "Paper" or playerHand == "Scissors"):
                break
            
            else:
                print("Invalid input. Try Again")
                
    # Generate computer pick
    computerHand = random.choice(Possible_Hands)
    
    
    # print results 
    print("Your hand: " , playerHand)
    print("CPU hand: " , computerHand)
    result = checkForWinner(playerHand , computerHand)
    
    if (result == "Player"):
        player_score += 1
        
    elif (result == "CPU"):
        CPU_score += 1
        
    else:
        tie_score +=1
    print("Your Score: ",player_score, "CPU: ",CPU_score , "Ties: ",tie_score)
    
    
    print("Game Over! Thank you for Playing")