import random,time,os

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "downton", "anime", "Fortnite", "Among", "naruto", "hangman", "sheldon", "roblox", "Leaf", "Ichigo","Sasuke", "School", "Apple", "Phone", "Games", "Money"]

wordChosen = random.choice(listOfWords).lower()

Guess = []
print(wordChosen)


print("Welcome to my hangman games")
print()
print()
time.sleep(2)
os.system("clear")

live = 6

while True:
  print(f"Here Will be place all the letters that you haved tried guessing:{Guess}")
  print()
  print()
  if live == 6:
      print("""
  +---+
  |   |
      |
      |
      |
      |
=========""")
  elif live == 5: 
    print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========(""")
  elif live == 4: 
    print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""")
  elif live == 3: 
    print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
========="""),
  elif live == 2: 
    print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""")
  elif live == 1: 
    print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""")

  print()
  letter = input("Chose a letter: ").strip().lower()
  if letter in Guess:
    print("You have already guess this letter")
    print()
    print()
    time.sleep(2)
    os.system("clear")
    continue

  Guess.append(letter)
    
  if letter in wordChosen:
    print(f"YOU ARE CORRECT!!! {letter} is indeed a letter of the word :)")
    
    allLetters = True
    for i in wordChosen:
      if i in Guess:
        print(i, end="")
      else:
        print("_", end="")
        allLetters = False
    print()
    print()
    print()
    
  elif letter not in wordChosen:
    print(f"saldy {letter} is not in the word :(")
    print()
    live -= 1
    print(f"You have lost a live and currently have {live} left")
    print()
    print()

    allLetters = True
    for i in wordChosen:
      if i in Guess:
        print(i, end="")
      else:
        print("_", end="")
        allLetters = False
    print()
    print()
    print()
    
  
    
      
  time.sleep(3)
  os.system("clear")

  
  if allLetters:
    print(f"YOU DID. YOU WON with {live} lives left")
    break
    exit()


  if live == 0:
    print("GAME OVER")
    print()
    print("""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========""")
    print()
    print("Click run to restart")
    break
    exit()

