#Hi I'm here

guesses = []
guesscount = 0
while True:
  password = input("Enter password: ")

  if password == "sui12345":
    guesscount+=1
    print("Access granted!")
    print(f"It took you {guesscount} tries...")
    break
  else:
    guesscount += 1
    print("Access denied!")
    guesses.append(password)
    print("You have already guessed:")
    for i in range(guesscount): 
      print(guesses[i])

input("Welcome back [ENTER]")
input("")