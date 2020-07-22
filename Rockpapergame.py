print("Rock = a\nPaper = b\nScissors = c\n")

a = "rock"
b = "paper"
c = "scissors"

while True:
    cont = input("New game? [Y/N]\n")
    if cont == "N":
        break
    else:
        p1 = input("Player 1: ")
        p2 = input("Player 2: ")
        if (p1, p2) == ("a", "c") or (p1, p2) == ("b", "a") or (p1, p2) == ("c", "b"):
            print("Player 1 wins!")
        elif (p1, p2) == ("c", "a") or (p1, p2) == ("a", "b") or (p1, p2) == ("b", "c"):
            print("Player 2 wins!")
        elif (p1, p2) != ("a", "b", "c"):
            print("Invalid selection!")
        else:
            print("It's a draw!")