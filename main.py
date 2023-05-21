import random,os,sys
from time import sleep
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"


def write(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.1)

gold = 50
troop = 0
level = 1


write("welcome to:")
sleep(3)
os.system('clear')

print(cyan + """
__________   |    |   |=======
     |       |    |   |   
	 |       |----|   |======
	 |       |    |   |
	 |       |    |   |=======


\				 /     /\  	   |--\  |--\  |=|  |\    |   /-----
 \      /\      /     /  \	   |--/  |--/  | |  | \   |  |
  \    /  \    /     /====\    |\    |\    | |  |  \  |  |    ___
   \  /    \  /     /      \   | \   | \   | |  |   \ |  |      |
    \/      \/     /        \  |  \  |  \  |=|  |    \|   \_____|


|  /   |=|  |\    |  /-----   |==\	   /-----\    |\        /|
| /    | |  | \   | |         |   \   /       \   | \      / |
|<     | |  |  \  | |    ___  |    | | 		   |  |  \    /  |
| \    | |  |   \ | |      |  |   /   \ 	  /   |   \  /   |
|  \   |=|  |    \|  \_____|  |==/     \_____/    |    \/    |


A risk game developed by @VulcanWM, @Name12, and @suryan1234 
""" + white)
sleep(6)
os.system('clear')
def demo():
  write(Orange + "\nAfter Kronos betrays you, you find yourself as an emperor of a kingdom. There are a lot of other kingdoms around to you, and your goal is to conquer them all and become the mightest emperor in the world")
  write(Orange + "\nYou will have 50 golden coins at the start of the game. you can use your coins to buy troops to attack other kingdoms, or you can use your coins to upgrade your troops to make them stronger. What is stronger, you say? well, the amounts of your troops are equal to the difference between the levels times the amount of troops you have. so, if you have a higher level than your opponent, you will have more troops than you actually do. but, if your opponent have higher troops than you, you will have less troops than you actually have.")
  write(Orange + "\nTo win the game, you have to conquer all the kingdoms. make your moves carefully because some kingdoms are stronger than others. but the greater the risk, the better the rewards. attacking other kingdoms can give you troops and even gold. but make sure not to spend all your golds at once because if you lose a battle, you will lose lots if not all of the troops that you used in that battle.")
  write(Orange + "\nThis will be a cruel world, and we wish you good luck.")
  write(Orange + "\nSo brace your self for " + cyan + "the warring kingdoms.")
  input(Cyan + "\n-->")
os.system("clear")
demoornot = input("Do you want to see the rules and the demo? (y,n)\n")
if demoornot == "y":
  demo()
os.system("clear")
lost = False
i = "="
while troop > -1 and lost == False and gold > -1:
  print(yellow + i*10,"the Warring Kingdom",i*10 + blue)
  print("you have",gold,"golden coins")
  print("you havre",troop,"troops")
  print("your army is at level", level)
  print(cyan + "a: " + Orange + "buy troops")
  print(cyan + "b: " + Orange + "upgrade troops")
  print(cyan + "c: " + Orange + "invade other kingdoms")
  user_input_choice = input(green + "what do you want to do\n")
  os.system('clear')
  if user_input_choice =="a":
    print(cyan + "troops: " + Orange + "1 coin")
    user_input_troops_amount = input(green + "How many troops do you want:")
    while not (user_input_troops_amount.isdigit() and 0<int(user_input_troops_amount)<10):
      print(red + "That is not a valid answer.")
      user_input_troops_amount = input(green + "How many troops do you want:")
    if int(user_input_troops_amount) >= 0:
      y_or_n = input(red + "are you sure you want to buy troops (y/n)")
      if y_or_n == "y":
        troop = int(user_input_troops_amount) + troop
        gold = gold - int(user_input_troops_amount)
        print("purchase successful")
        input(Cyan + "\n-->")
        os.system('clear')

  if user_input_choice == "b":
    print(cyan,"level",str(level + 1),Orange,str(level*5+25-5),"coin")
    user_input_level_upgrade = input("do you want to upgrade your level (y/n)")
    if user_input_level_upgrade == "y":
      gold -= level*5+25
      level += 1
      os.system('clear')
  if user_input_choice == "c":
    number = random.randint(1,20)
    if number == 1 or number == 2 or number == 3 or number == 4 or number == 5 or number == 6 or number == 7 or number == 8 or number == 9 or number == 10:
      print("You defeated a kingdom.")
      cots = "coins","troups", "both"
      cot = random.choice(cots)
      if cot == "coins":
        coina = random.randint(1,10)
        gold = coina + gold
        print("You got", coina, "gold")
      elif cot == "troups":
        troopa = random.randint(1,10)
        troup = troopa + troop
        print("You got",troopa,"troops")
      else:
        coina = random.randint(1,10)
        gold = coina + gold
        print("You got", coina, "gold")
        troopa = random.randint(1,10)
        troop = troop + troopa
        print("You got",troopa,"troops")
    elif number == 11:
      print("Both of the armies got tired. They both retreated.")
      troopless = random.randint(1,10)
      troop = troop - troopless
      print("You lost", troopless, "troops")
      input(Cyan + "\n-->")
    else:
      print("You got defeated.")
      lost = True
if lost == True:
  print("Your kingdom got invaded by another kingdom. You lost the game!")
elif gold < 0:
  print("You have gone bankrupt. You end up living as a beggar for the rest of your life.")
else:
  print("A person who lived in your kingdom, challenged you, and you lost the challenge, you are not emperor any more.")
