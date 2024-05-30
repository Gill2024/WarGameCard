from CardGame import CardGame
# Display welcome message and instructions for the game.
welcome_message = input("🃏🎉 Welcome to the Ultimate War Of Cards! 🎉🃏\n"
                        "--------------------♠️♦️♣️♥️--------------------\n"
                        "Get ready for an exciting battle of wits and luck!\n"
                        "Here's how to play:\n"
                        "1. Each player will receive a deck of cards.\n"
                        "2. In each round, both players draw the top card from their deck.\n"
                        "3. The player with the higher value card wins the round and takes both cards.\n"
                        "4. The game consists of 10 thrilling rounds.\n"
                        "5. The player with the most cards at the end of the game is the winner!\n"
                        "--------------------------------------------\n"
                        "Press Enter to start the game and may the best player win!\n")

# Create a new game, input the names of the players, each gets 26 cards.
game1=CardGame(input('Enter name of player 1:'),input('Enter name of player 2:'),26)
print(game1)  # Print the initial state of the game.

# Play 10 rounds of the game.
for i in range(10):
    # Each player plays one card from their hand.
    card_player1=game1.player1.get_card()
    card_player2=game1.player2.get_card()

    # Print the cards played by each player.
    print(f'{'_'*30}\n{game1.player1.player_name}`s card: {card_player1}\n{game1.player2.player_name}`s card: {card_player2}')

    # Determine the round winner and update their deck.
    if card_player1>card_player2:
        game1.player1.add_card(card_player1)
        game1.player1.add_card(card_player2)
        print(f"{game1.player1.player_name} wins the round!")
    if card_player2>card_player1:
        game1.player2.add_card(card_player1)
        game1.player2.add_card(card_player2)
        print(f"{game1.player2.player_name} wins the round!")

# Determine and print the game winner or if it ended in a draw.
if game1.get_winner()==None:
    print('_'*30,'\n🤝\nThe game ended in a draw.')
else:
    print(f'{'_'*30}\n🎉🏆🎉🏆🎉🏆\nTHE WINNER IS- {game1.get_winner()}')
