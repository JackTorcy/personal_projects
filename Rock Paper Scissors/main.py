#importing so that we can randomise the computers choice
import random

#while loop so that we can play again
while True:
    
    #selects the winner of the round and returns outcome
    def winner(playerChoice, computerChoice):
        if playerChoice == 'R':
       
            if computerChoice == 'R':
                outcome = "Draw"
            elif computerChoice == 'P':
                outcome = "You Lose!"
            else:
                outcome = "You Win!"
        elif playerChoice == 'P':
        
            if computerChoice == 'P':
                outcome = "Draw"
            elif computerChoice == 'S':
                outcome = "You Lose!"
            else:
                outcome = "You Win!"
        elif playerChoice == 'S':
        
            if computerChoice == 'S':
                outcome = "Draw"
            elif computerChoice == 'R':
                outcome = "You Lose!"
            else:
                outcome = "You Win!"
        else:
            outcome = "Please select a valid choice!"

        return outcome    
    
    playerScore = 0
    computerScore = 0

    #simple entrance message
    print("Welcome to rock paper scissors!")
    input("   Press any key to continue.  ")
    
    #round number selection
    print("Please select how many rounds you would like to play: ")
    print("Press '1' for just 1 round")
    print("Press '3' for a best of 3")
    print("Press '5' for a best of 5")
    roundNum = input("Your selection: ")
    
    #tests if roundNum is either a 1, 3 or 5
    while True:
        if roundNum in('1', '3', '5'):
            break
        else:
            roundNum = input("Please enter a valid number of rounds: ")
            continue
    
    #sets the round number
    if roundNum == '1':
        i = 1
    elif roundNum == '3':
        i = 2
    else:
        i = 3
    
    #determins whether or not to run code based on roundNum input
    while playerScore < i and computerScore < i:
        #assigns computerChoice a random option each loop
        possibleOutputs = ['R', 'P', 'S']
        computerChoice = random.choice(possibleOutputs)
        
        #let the player select an option and assign their choice to variable
        print("Please enter one letter for either [R]ock, [P]aper or [S]cissors")
        playerChoice = input("Your choice: ")
        
        #prints out the result of the function
        print(winner(playerChoice, computerChoice))
        
        #adds a point to the winners score or does nothing if draw/invalid choice
        if (winner(playerChoice, computerChoice) == 'You Win!'):
            playerScore += 1
        elif(winner(playerChoice, computerChoice) == 'You Lose!'):
            computerScore += 1
        
        #prints out computers choice and current scores
        print("The computer chose: " + computerChoice)
        print("Your score is: " + str(playerScore))
        print("The computers score is: " + str(computerScore))
        
    #determines the winner of the game
    if computerScore > playerScore:
        print("LOSER!!!")
    elif playerScore > computerScore:
        print("WINNER!!!")
    
    #option to play again
    playAgain = input("Would you like to play again? Y/N : ")

    #checks for valid input
    while True:
        if playAgain in('Y', 'N'):
            break
        else:
            playAgain = input("Please enter a valid option")
            continue
    
    #either plays again or exits
    if playAgain == 'Y':
        continue
    else:
        print("Thank you for playing!")
        break

    
            

    

