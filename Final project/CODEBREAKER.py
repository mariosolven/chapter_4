import random # module to be able to choose random numbers.

cont = 1 # for our game selection.

# Initial screen of the game.
while cont == 1:
  print("\n*****************")
  print("* CODE BREAKER *")
  print("*****************")
  print("\nInstructions: \nDecipher a numerical code given the necessary digits for the chosen level. The harder the level, the code will be a little longer. If you guess a code digit and it is in the correct position, it will be marked as a hit, but if it is not in the correct position, it will be marked as a match. Good luck.")
  print("\nDifficulty: \n1 = Easy | 2 = Medium | 3 = Hard")

  diff = int(input("\nWrite the Difficulty number of your choice: ")) # input where the user choose the game difficulty.

  ## asigning game difficulties values.
  if diff == 1:
    total_digits = 3
  elif diff == 2:
    total_digits = 4
  elif diff == 3:
    total_digits = 5

  digits = ('0','1','2','3','4','5','6','7','8','9') # we create a tupple of the symbols avaliables to be typed as character strings.
  code = '' # variable where the code will be stored.

  for i in range(total_digits):
      choosen = random.choice(digits) # random function to select a random value from our digits tupple.
      while choosen in code: # to avoid repeated characters.
        choosen = random.choice(digits)
      code = code + choosen # to concatenate our choosen digits next to each other in the variable code.

  print("\n<You have to guess a",total_digits,"different digit code.>") # instructions based on the choosen difficulty.
  proposal = input("\nWrite your code: ") # game started.
  attempts = 1 # proposal counter starting at 1.

  # while loop to check if the typed number is wrong.
  while proposal != code:
      attempts = attempts + 1 # if you are wrong, this counter increases.
      hits = 0
      matches = 0
      # for loop to check if the typed number is right.
      for i in range(total_digits): # variable i which is the position of the code.
          if proposal[i] == code[i]: # comparing the typed number with the assigned code.
              hits = hits + 1 # our counter increases.
          elif proposal[i] in code: # if we have some number that match with the code but is in a wrong position.
              matches = matches + 1
      
      print ("\nYour code has",hits,"hits and",matches,"matches. \nHint: check the order of some numbers.") # printing our hits and matches to help us guessing.
      print("----------------------")
      proposal = input("\nSuggest another code: ") # input to accept another attempt.
  
  print ("\n\nCONGRATS! You guess the code in",attempts,"attempts.") # Priting congrats in case you won.
  print("Do you want to play again?: \n\n1 = Continue | 0 = Exit")
  cont = int(input("\nYour answer: "))