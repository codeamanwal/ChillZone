import random
from playsound import playsound

command=input("Liten to music or play rock, paper, scissor :) ?(music/play)")

if(command=="play"):
  options = ("rock", "paper", "scissors")
  running = True

  while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False
        print("Thanks for playing!")




elif(command=="music"):
    print("No. of available songs\n1.Duniyaa\n2.Tu Maan Meri Jaan")
    order = input("Enter the choice of music you want to  play: ")
    if "1" in order:
       playsound('C:\\Users\\DELL\\Music\\Duniyaa.mp3')
    elif "2" in order:
       playsound('C:\\Users\\DELL\\Music\\Tu Maan Meri Jaan.mp3')
       
    print("Thank You")   




