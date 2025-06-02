import random #import random module to help randomize and shuffle deck when dealing cards

#This create a standard 52-card Blackjack deck
#Face cards(Jack, Queen, King) are represented as 10's in the function
#Aces are represented as 11 now and will change to 1 in a later function if needed.
def create_deck():
    return [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

#Function removes 1 card from the top of deck
def deal_card(deck):
    return deck.pop()

#This function calculate the total value of a hand
#Also adjusts Ace value from 11 to 1 if needed by seeing if total from hand exceeds 21
def calculate_total(hand):
    total = sum(hand)
    ace_count = hand.count(11)
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1
    return total

#Displays the player and/or dealer's hand and the total as well
def display_hand(name, hand):
    print(f"{name}'s hand: {hand} (Total: {calculate_total(hand)})")

#Main function that plays one round of Blackjack
def play_game():
    #Create and shuffles a new deck for the game
    deck = create_deck()
    random.shuffle(deck)

    #Deals two cards to both player and dealer
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    #Calculate the initial total for both dealer and player's hand.
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    #Checks for intial/natural Blackjack 
    if player_total == 21 and dealer_total == 21:
        print("Player and Dealer both have Blackjack. Tie!") 
        return
    elif player_total == 21:
        print("You have a Blackjack. You win!")
        return
    elif dealer_total == 21: 
        print("Dealer has a Blackjack. You lose!")
        return
    else:
        print("No one has a blackjack. Continue playing")

    #Player's turn/round
    #Displays player's hand and total while also giving player option to either "Hit" or "Stand"
    while True:
        display_hand("Player", player_hand)
        choice = input("'Hit' or 'Stand'?").strip().lower() #Makes sure to strip any spaces and all characters a lowercase
        if choice == "hit":  #If player hits
            player_hand.append(deal_card(deck)) #Adds a card to player's hand
            player_total = calculate_total(player_hand) #Calculate new player's total
            if player_total > 21:  #If player busts
                display_hand("Player", player_hand)
                print("Total exceeds 21. You busted. You lose!")
                return #Ends game immdediatly
            elif player_total == 21: #If player gets Blackjack from htting
                display_hand("Player", player_hand)
                print("You hit 21! Your turn ends")
                break #This is to prevent player from hitting if they hit blackjack
        elif choice == "stand": 
            break #If player chooses to stand and stop getting cards, breaks out of while loop
        else: #Makes sure no other responses than hit or stand are valid
            print("Invalid input. Please type 'hit' or 'stand'.")

    #Dealer's Turn/Round
    print("\nDealer's turn...")
    display_hand("Dealer", dealer_hand)

    #Dealer must keep hiting to at least 17 or bust. This while loop implements this rule. 
    while calculate_total(dealer_hand) < 17: #if the total of dealer's hand is less than 17, makes the dealer hit. 
        print("Dealer hits.")
        dealer_hand.append(deal_card(deck)) # Adds card to dealer's hand after hitting
        display_hand("Dealer", dealer_hand)

    #Final calculations before comparing and stating an outcome.
    dealer_total = calculate_total(dealer_hand)
    player_total = calculate_total(player_hand)

    #Determine outcomes based on final totals
    if player_total == 21:
        print("You got a Blackjack. You win!")
    elif dealer_total == 21 and player_total == 21:
        print("Player and Dealer both have Blackjack. Tie!")
    elif dealer_total == 21:
        print("Dealer got a Blackjack. You lose!")
    elif dealer_total > 21:
        print("Dealer busted. You win!")
    elif dealer_total > player_total:
        print("Dealer wins. You lose!")
    elif dealer_total < player_total:
        print("You win!")
    else:
        print("Tie!")

#Function allows the player to replay game multiple times.
def main ():
    while True:
        play_game() #Initiates one full game
        again = input("Play again? (Yes/No): ").strip().lower() #Makes sure to strip any spaces and all characters a lowercase
        if again != "yes": 
            break #Exit the while loop if player doesn't type "yes"
    print("Thank you for playing!")



if __name__ == "__main__":
    main()


