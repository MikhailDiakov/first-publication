import random as r


def main():
    print("let's start")
    count_people = 0
    count_dealer = 0
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10] * 4
    r.shuffle(cards)
    print(f"your first card is {cards[0]}")
    count_people = cards[0]
    cards.pop(0)
    print(f"the dealer's first card is {cards[0]}")
    count_dealer = cards[0]
    cards.pop(0)
    while True:
        choice = input("will you take the card again(choice Y/N)? ")
        if choice == "Y":
            if count_people > 10 and cards[0] == 11:
                cards[0] = 1
            count_people += cards[0]
            print(f"you got a card {cards[0]}, your count is {count_people}")
            cards.pop(0)
            if count_people > 21:
                print("you lose")
                break
            elif count_people == 21:
                print("you win!")
                break
        elif choice == "N":
            print(f"you have {count_people} points")
            break
        else:
            print("enter Y if your answer is YES, and N if your answer is NO")

    if count_people < 21:
        print(f"dealer has {count_dealer} points")
        while True:
            if count_dealer <= count_people:
                if count_dealer > 10 and cards[0] == 11:
                    cards[0] = 1
                count_dealer += cards[0]
                print(f"the dealer got a card {cards[0]}, his count is {count_dealer}")
                cards.pop(0)
                if count_dealer > 21:
                    print("you win!")
                    break
                elif count_dealer == 21 or count_dealer > count_people:
                    print("you lose!")
                    break
                elif count_dealer == count_people and count_dealer >= 19:
                    print("you have the same number of points!")
                    break


if __name__ == "__main__":
    main()
