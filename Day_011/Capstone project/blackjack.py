import random

# The ASCII Art Logo
logo = """
.------.            _     _            _    _ack      
|A_  _ |           | |   | |          | |  (_)         
|( \/ )|  _ __  ___| | __| | __ _  ___| | ___  __ _  ___ 
| \  / | | '_ \/ __| |/ _` |/ _` |/ __| |/ / |/ _` |/ __|
|  \/ A| | |_) \__ \ | (_| | (_| | (__|   <| | (_| | (__ 
`------' | .__/|___/_|\__,_|\__,_|\___|_|\_\_|\__,_|\___|
         | |                                             
         |_|                                             
"""


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards_list):
    """Takes a list of cards and returns the score, handling Blackjack and Aces."""
    # Check for a natural Blackjack (Ace + 10-value card with only 2 cards)
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0  # Using 0 as a special code for Blackjack

    # If score is over 21 and there's an Ace (11), change it to a 1
    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)


def compare(player_score, dealer_score):
    """Compares the final scores and returns the match result."""
    if player_score == dealer_score:
        return "It's a draw! 🤝"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack! 😱"
    elif player_score == 0:
        return "Win with a Blackjack! 😎"
    elif player_score > 21:
        return "You went over. You lose! 💥"
    elif dealer_score > 21:
        return "Opponent went over. You win! 😁"
    elif player_score > dealer_score:
        return "You win! 🏆"
    else:
        return "You lose! 😢"


def play_game():
    print(logo)

    player_cards = []
    dealer_cards = []
    is_game_over = False

    # Deal initial 2 cards to player and dealer
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    # --- PLAYER'S TURN ---
    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"   Your cards: {player_cards}, current score: {player_score}")
        print(f"   Dealer's first card: {dealer_cards[0]}")

        # End turn if someone has Blackjack or player busts
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to stand: ").lower()
            if user_should_deal == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    # --- DEALER'S TURN ---
    # Dealer must hit if their score is less than 17 (and player hasn't busted)
    while dealer_score != 0 and dealer_score < 17 and player_score <= 21:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    # --- FINAL REVEAL ---
    print("\n--- FINAL RESULTS ---")
    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Dealer's final hand:AC {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))


# --- MAIN REPLAY LOOP ---
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)  # Clears the terminal screen for a fresh round
    play_game()