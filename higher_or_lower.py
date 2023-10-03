# Step 1: Print ASCII art of Logo and VS
# Step 2: Compare A, select a random sequence of the dict
# Step 3: For each loop, and compare downwards
# Step 4: Use bool to compare A or B and continue
# Step 5:
# Step 6: If answer is wrong, then quit the program

import random
from game_data import data
from art import logo, vs
from replit import clear

# Random Sequence
sequence = []
for i in range(len(data)):
  sequence.append(random.sample(range(len(data)), 1))


# Check Answer function
def check_followers(a, b):
  if a["follower_count"] > b["follower_count"]:
    return "a"
  else:
    return "b"


def show_questions(a, b):
  print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
  print(vs)
  print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")


def format_data(account):
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}."


print(logo)
score = 0

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
  account_b = random.choice(data)

# First number of the sequence list.
for j in range(len(sequence)):
  a = data[sequence[j - 1][0]]
  b = data[sequence[j][0]]
  
  try:
    
    show_questions(a, b)
    answer = (
      input("Who has more followers? Type 'A' or 'B'?: ")).lower().strip()
    if answer == check_followers(a, b):
      score += 1
      clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      pass
    else:
      clear()
      break
  except EOFError:
    print(logo)
    print("You ended abruptly..")
    break
    
print(logo)
print(f"Sorry, that's wrong. Final score: {score}.")
