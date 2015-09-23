decision1 = raw_input("Player 1: Rock, paper or scissors?").lower()
decision2 = raw_input("Player 2: Rock, paper or scissors?").lower()

if (decision1 == "rock" and decision2 == "rock"):
    print "It's a tie!"
elif (decision1 == "rock" and decision2 == "paper"):
    print "Player 2 wins!"
elif (decision1 == "rock" and decision2 == "scissors"):
    print "Player 1 wins!"
elif (decision1 == "rock" and decision2 == "lizard"):
    print "Player 1 wins!"
elif (decision1 == "rock" and decision2 == "spock"):
    print "Player 2 wins!"
elif (decision1 == "paper" and decision2 == "rock"):
    print "Player 1 wins!"
elif (decision1 == "paper" and decision2 == "paper"):
    print "It's a tie!"
elif (decision1 == "paper" and decision2 == "scissors"):
    print "Player 2 wins!"
elif (decision1 == "paper" and decision2 == "lizard"):
    print "Player 2 wins!"
elif (decision1 == "paper" and decision2 == "spock"):
    print "Player 1 wins!"
elif (decision1 == "scissors" and decision2 == "rock"):
    print "Player 2 wins!"
elif (decision1 == "scissors" and decision2 == "paper"):
    print "Player 1 wins!"
elif (decision1 == "scissors" and decision2 == "scissors"):
    print "It's a tie!"
elif (decision1 == "scissors" and decision2 == "lizard"):
    print "Player 1 wins!"
elif (decision1 == "scissors" and decision2 == "spock"):
    print "Player 2 wins!"
elif (decision1 == "lizard" and decision2 == "rock"):
    print "Player 2 wins!"
elif (decision1 == "lizard" and decision2 == "paper"):
    print "Player 1 wins!"
elif (decision1 == "lizard" and decision2 == "scissors"):
    print "Player 2 wins!"
elif (decision1 == "lizard" and decision2 == "lizard"):
    print "It's a tie!"
elif (decision1 == "lizard" and decision2 == "spock"):
    print "Player 1 wins!"
elif (decision1 == "spock" and decision2 == "rock"):
    print "Player 1 wins!"
elif (decision1 == "spock" and decision2 == "paper"):
    print "Player 2 wins!"
elif (decision1 == "spock" and decision2 == "scissors"):
    print "Player 1 wins!"
elif (decision1 ==" spock" and decision2 == "lizard"):
    print "Player 2 wins!"
elif (decision1 == "spock" and decision2 == "spock"):
    print "It's a tie!"
else:
    print "invalid input"
