# Create a magic8.py program that can answer any Yes or No questions with a different fortune/advice each time it executes.
# Magic 8 Ball 🎱

import random

ball = random.randint(1, 9)

question = input('Question: ')

if ball == 1:
  answer = "Yes - definitely"
elif ball == 2:
  answer = "It is decidedly so"
elif ball == 3:
  answer = "Without a doubt"
elif ball == 4:
  answer = "Reply hazy, try again"
elif ball == 5:
  answer = "Ask again later"
elif ball == 6:
  answer = "Better not tell you now"
elif ball == 7:
  answer = "My sources say no"
elif ball == 8:
  answer = "Outlook not so good"
else:
  answer = "Very doubtful"

print("Question:      " + question)
print("Magic 8 Ball:  " + answer)
