import random

def GuessingGame():
  number = int(random.randint(1,10))
  WhatsYourNumber=int(input("Whats your number?"))
  while WhatsYourNumber != number:
    print("keep guessing")
    WhatsYourNumber=int(input("Whats your number"))
    if WhatsYourNumber == number:
      print("winner")
      break
GuessingGame()
