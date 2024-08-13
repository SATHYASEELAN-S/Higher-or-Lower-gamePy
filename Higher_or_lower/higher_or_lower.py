import random,os
from art import logo,vs
from game_data import data

score=0
a=random.choice(data)
b=random.choice(data)
flag=True
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def check(guess,a_count,b_count):
    if a_count>=b_count:
        return guess=='a'
    else:
        return guess=='b'

while flag:
    print(logo)
    if score>0:
        print("You're right! Current score: ",score)
    print(f"Compare A:{a['name']},a {a['description']},from {a['country']}")
    print(vs)
    
    print(f"Against B:{b['name']},a {b['description']},from {b['country']}")
    guess=input("Who has more followers? Type 'A' or 'B':").lower()
    clear_screen()
    if check(guess,a['follower_count'],b['follower_count']):
        score+=1
        if b['follower_count']>a['follower_count']:
            a=b
    else:
        break
    b=random.choice(data)


print(logo)
print("Sorry! Wrong, Your Score is ",score)
