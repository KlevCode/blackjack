import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card():
  user_cards = random.choices(cards, k=2)
  computer_cards = random.choices(cards, k=2)
  print(user_cards, computer_cards)

deal_card()

def calculate_score(deal_card):
  sum_user_cards = sum(user_cards)
  sum_computer_cards = sum(computer_cards)
  if user_cards == [11, 10] or user_cards == [10, 11]:
    return 0
    print("User wins with blackjack!")
  elif computer_cards == [11, 10] or computer_cards == [10, 11]:
    return 0
    print("Computer wins with blackjack!")
  elif sum_user_cards > 21:
    print("Computer wins!")
  print(sum_user_cards, sum_computer_cards)


calculate_score(deal_card)


#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

