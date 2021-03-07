from random import seed
from random import randint

print('Welcome to our Disney Adventure!\nEven in the Disney world can get sick sometimes.\nPlease help us stay safe and healthy by making the right choice!\n')
name = input('Before we begin... what is your name?\n')
print('Hi, ' +  name + "!")
print('\n')

movies = ["Sleeping Beauty", "Cinderella", "Tangled", "Frozen", "Aladdin", "Snow White and the Seven Dwarfs", "Beauty and the Beast"]
characters = [["Princess Aurora", "Prince Phillip", "Maleficent"], ["Cinderella", "Prince Charming", "Drizella"], ["Rapunzel", "Flynn Rider", "Gothel"], ["Elsa", "Anna", "Olaf"], ["Aladdin", "Jasmine", "Genie"], ["Snow White", "Evil Queen", "Dopey"], ["Beast", "Belle", "Gaston"]]

print('Please choose a movie from the following list by typing the number!')
index = 1
for movie in movies:
  print(str(index) + ". " + movie)
  index = index + 1
index = input()
while int(index) < 1 or int(index) > 7:
  index = input('Oops! Invalid Index! Please enter a number from 1 to 7.\n')
movie = int(index) - 1

print('\nPlease choose a character you would like to help from the following list - by typing another number!')
index = 1
for character in characters[movie]:
  print(str(index) + ". " + character)
  index = index + 1
index = input()
while int(index) < 1 or int(index) > 3:
  index = input('Oops! Invalid Index! Please enter a number from 1 to 3.\n')
character = characters[movie][int(index) - 1]
print('\nHi, ' + character + "! Let the adventure begin!")

scenarios = ["\nOops! You have a high fever.", "\nIt seems like you have a cough!", "\nHmmm, for some reason you can't seem to smell or taste anything?", "\nOuch! Your head starts to hurt!", "\nUh oh! Looks like some people are walking towards you.", "\nSomeone near you is coughing!", "\nYour friend just tested positive for COVID-19!", "\nYour friend just invited you to a party at her house!", "\nYou forgot to wear a mask outside today."]

response1 = ["Let's go get tested for COVID-19.", "Let's go out and have some fun!"]
response2 = ["That's not a big deal.", "I'll go put on a mask."]
response3 = ["That's not a problem!", "I'll stay home and quarantine myself."]
response4 = ["I'll go take some rest and get tested later.", "It's not that serious, don't worry about it!"]
response5 = ["Let's stay away from her!", "She looks fine!"]
response6 = ["Don't worry about it, she said she's not positive.", "Oh no! I can't be around her!"]
response7 = ["Yay! I'm so excited for it!", "No. This is going to worsen the pandemic."]
response8 = ["We don't need that thing, right?", "I'll go back and get it."]

choice = 'yes'
while choice != 'no':
  question = randint(0, 8)
  print(scenarios[question])
  ind = 1
  if question == 0 or question == 1 or question == 2 or question == 3:
    rand = randint(1, 4)
    if rand == 1:
      for x in response1:
        print(str(ind) + ". " + x)
        ind = ind + 1
      num = input('What should you do? (Type 1 or 2)\n')
      if int(num) == 1:
        print('Way to go ' + character + '!\n')
      elif int(num) == 2:
        print('No. Please go get tested.\n')
      else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

    elif rand == 2:
      for x in response2:
        print(str(ind) + ". " + x)
        ind = ind + 1
      num = input('What should you do? (Type 1 or 2)\n')
      if int(num) == 2:
        print('Way to go ' + character + '!\n')
      elif int(num) == 1:
        print('No. Please put on a mask.\n')
      else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

    elif rand == 3:
      for x in response3:
        print(str(ind) + ". " + x)
        ind = ind + 1
      num = input('What should you do? (Type 1 or 2)\n')
      if int(num) == 2:
        print('Way to go ' + character + '!\n')
      elif int(num) == 1:
        print('No. Please stay home.\n')
      else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

    else:
      for x in response4:
        print(str(ind) + ". " + x)
        ind = ind + 1
      num = input('What should you do? (Type 1 or 2)\n')
      if int(num) == 1:
        print('Way to go ' + character + '!\n')
      elif int(num) == 2:
        print('No. Please stay home.\n')
      else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

  elif question == 4 or question == 5 or question == 6:
    rand = randint(5, 6)
    if rand == 5:
      for x in response5:
        print(str(ind) + ". " + x)
        ind = ind + 1
      num = input('What should you do? (Type 1 or 2)\n')
      if int(num) == 1:
        print('Way to go ' + character + '!\n')
      elif int(num) == 2:
        print('No. Please stay away from her.\n')
      else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

    elif rand == 6:
      for x in response6:
        print(str(ind) + ". " + x)
        ind = ind + 1
      num = input('What should you do? (Type 1 or 2)\n')
      if int(num) == 2:
        print('Way to go ' + character + '!\n')
      elif int(num) == 1:
        print('No. Please stay away from her.\n')
      else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

  elif question == 7:
    for x in response7:
      print(str(ind) + ". " + x)
      ind = ind + 1
    num = input('What should you do? (Type 1 or 2)\n')
    if int(num) == 2:
      print('Way to go ' + character + '!\n')
    elif int(num) == 1:
      print('No. Please stay home.\n')
    else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

  elif question == 8:
    for x in response8:
      print(str(ind) + ". " + x)
      ind = ind + 1
    num = input('What should you do? (Type 1 or 2)\n')
    if int(num) == 2:
      print('Way to go ' + character + '!\n')
    elif int(num) == 1:
      print('No. Please wear a mask when you are outside.\n')
    else:
        print("Oops! Invalid Index! Please enter a number from 1 to 2.")

  choice = input('Do you want to continue? Please type yes or no.\n')

  while choice != 'yes' and choice != 'no':
    choice = input("Invalid response. Please type yes or no.\n")
  
print('\nQuitting game. \nWe look forward to our next adventure with you!\n')
