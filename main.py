def guessing_game():
  
  target_number = 6
  num_guesses = 0
  max_guesses = 10
  print("I'm thinking of a number between 1 and 12 (my birthmonth). You have 10 guesses to find it try to guess it.")

  while num_guesses < max_guesses:
    try:
      guess = int(input("Enter your guess: "))
    except ValueError:
      print("i said month as a nomber. Please enter an integer.")
      continue

    num_guesses += 1

    if guess == target_number:
      print(f"Congratulations! it's the month 6 june You guessed the number in {num_guesses} guesses.")
      return

    elif guess < target_number:
      print("Your guess is too low zid chwia.")
    else:
      print("Your guess is too high n9es n9es.")

  print("You ran out of guesses. The month number was june ", target_number)

guessing_game()
