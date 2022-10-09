import datetime
import csv
import os
from math import ceil

# import learning variables
class vari:
    def __init__(self, name, value, exp):
        self.name = name
        self.value = value
        self.exp = exp

vars = []

readvari = csv.reader(open(os.getcwd()+'/.userdata/learnvars.csv', 'r'))



# IMPT

def impt(deck):
  # make a deck
  reader = csv.reader(open('import.txt', 'r'))
  writer = csv.writer(open('csv.mnak', 'w'))
  
  # import new cards into deck
  for row in reader:
    writer.writerow([row[0], row[1], 0, float(readvari[7][1]), 0, datetime.date.today()])

# INIT

# variables:
# learning steps (ls, range from 0-2)
# ease (the value that the intervals increase everytime "good" is picked, default 2.5x)
# last interval (the interval given for the last time the card was touched)
# due date (the next date at which the card will be reviewed)

# card structure
class flashcard:
  def __init__(self, term, defin, ls, ease, lastint, duedate):
    self.term = term
    self.defin = defin
    self.ls = ls
    self.ease = ease
    self.lastint = lastint
    self.duedate = duedate

# initialisation function
def init(deck):
  reader = csv.reader(open(os.getcwd()+'/.userdata/csv.mnak', 'r')) 
  
  # import csv into deck
  for row in reader:
    for ocard in deck:
      if ocard.term == row[0]:
        deck.remove(ocard) # remove old copy of card
    deck.append(flashcard(row[0], row[1], int(row[2]), float(row[3]), float(row[4]), row[5]))

# LEARN

def learn(deck):
  # variables:
  # learning steps (intervals when a card is first learned, 1m 10m 1d by default)
  learnsteps = [readvari[2][1], readvari[3][1], int(readvari[4][1])]
  # easy interval (time between picking easy and reviewing the card for the first time)
  easyint = int(readvari[5][1])
  # easy bonus (bonus multiplier to ease when easy picked, default 1.3)
  easybonus = float(readvari[8][1])
  # hard bonus (multiplier from last value, default 1.2)
  hardint = float(readvari[9][1])
  
  # FUNCTIONS
  # function to generate intervals
  def genints(card):
    match card.ls:
      case 0:
        ints = [learnsteps[0], str((int(learnsteps[0])+int(learnsteps[1]))/2), learnsteps[1], easyint]
      case 1:
        ints = learnsteps + easyint
      case 2:
        ints = ["10", ceil(card.lastint * card.ease, 0), ceil(card.lastint * card.ease), ceil(card.lastint * card.ease * card.easybonus)]
    for x in ints:
      if type(x) == int and x > int(readvari[6][1]):
        x = int(readvari[6][1])
  
  # function to print out intervals
  def printno(no):
    if type(no) == str:
      return(no + "m")
    elif type(no) == int:
      return(str(no) + "d")
  
  # function to schedule a new card
  def newint(card):
    # prompting user
    print("~~~~~~~~~~~~~~~~~~~~")
    input(f"term: {card.term}\n")
    print(f"definition: {card.defin}\n")
    option = int(input("enter 1-4 for:" + 
    f"\n1. again ({printno(genints(card)[0])})" + 
    f"\n2. hard ({printno(genints(card)[1])})" +
    f"\n3. good ({printno(genints(card)[2])})" +
    f"\n4. easy ({printno(genints(card)[3])})\n\n"))-1
    print("card delayed by:", printno(genints(card)[option]))
    if type(genints(card)[option]) == str:
      # rescheduling card
      try:
        queue[int(genints(card)[option])].append(card)
      except:
        while len(queue) < int(genints(card)[option])+1:
          queue.append([])
      queue[-1].append(card)
    else:
      # change data in deck
      for ocard in deck:
        if ocard.term == card.term:
          deck.remove(ocard) # remove old copy of card
      card.duedate = str(datetime.datetime(int(card.duedate[0:4]), int(card.duedate[5:7]), int(card.duedate[8:10])) + datetime.timedelta(days=genints(card)[option]))
      card.lastint = genints(card)[option]
      print("1 card less!")
      deck.append(card) # add new copy of card
    queue[0].remove(card) # remove card from queue
    match option:
      case 0:
        card.ls = 0
      case 1:
        pass
      case 2:
        if card.ls < 2:
          card.ls += 1
      case 3:
        card.ls = 2
        card.ease *= card.easybonus
    
  # count cards
  def cardnum():
    count = 0
    for x in queue:
      count += len(x)
    return count

  # SESSION
  # making queue
  queue = [[]]
  newcount = 0
  revcount = 0
  for card in deck:
    if card.duedate == str(datetime.date.today()):
      queue[0].append(card)
      match card.ls:
        case 2:
          revcount += 1
        case __:
          newcount += 1
    if newcount >= int(readvari[0][1]) or revcount >= int(readvari[1][1]):
      break
  
  # begin!
  print(f"hello! welcome to your learning session.\ntoday's card count: {cardnum()}.")
  
  while queue != []:
    for card in queue[0]:
      newint(card)
      if cardnum() > 0:
        print("remaining cards:", cardnum())
        if input("continue? (Y/n)") == "n":
          break
      else:
        print("good job! you finished the deck.")
    if queue[0] == []:
      queue.pop(0)

# SAVE

def save(deck):
  writecsv = csv.writer(open(os.getcwd()+'/.userdata/csv.mnak', 'w'))
  writetxt = open(os.getcwd()+'/.userdata/readme.txt', 'w')

  # save to 
  for x in deck:
    writecsv.writerow([x.term, x.defin, x.ls, x.ease, x.lastint, x.duedate])
    writetxt.write(x.term + "    " + x.defin)

# SETTINGS

for x in readvari:
  vars.append(vari(x[0], float(x[1]), x[2]))

string = ""
for x in range(len(vars)):
  vari = vars[x]
  string = string + vari.name + " (" + str(x) + ") - " + vari.exp + "\ncurrent value: " + str(vari.value) + "\n~~~~~~~~~~~~~~~~~~~~\n"

def settings():
  print(string)
  while 1: 
    comm = input("enter any number to change the value of its corresponding variable, 'help' to see the list of variables again or 'exit' to exit settings. ")
    match comm:
      case 'help':
        print(string)
      case 'exit':
        break
      case __:
        try:
          comm = int(comm)
          vari = vars[comm]
        except:
          print("invalid command. try again!")
        else:
          print(vari.name + " (" + str(int(comm)) + ") - " + vari.exp + "\ncurrent value: " + str(vari.value))
          while 1:
            newval = input("enter new value: ")
            try:
              float(newval)
            except:
              print("invalid. try again")
            else:
              vari.value = newval
              break
          print("\n")
          writevari = csv.writer(open(os.getcwd()+'/.userdata/learnvars.csv', 'w'))
          for x in vars:
            writevari.writerow([x.name, x.value, x.exp])

def guide():
  guidelist = {
    "faq" : "see frequently asked questions."
    "imexport" : "see instructions on how to import and export data."
  }
  for x in guidelist:
    print(x + ": " + guidelist[x])
  while 1:
    comm = input("\nenter the name of the guide you want to see, 'help' to see the list of guides again or 'exit' to exit guides.")
    match comm:
      case "help":
        print(guidelist)
      case "exit":
        break
      case __:
        try:
          f = open(os.getcwd()+'/.guides/'+comm+'.txt', 'r')
        except:
          print("invalid. try again")
        else:
          for line in f.readlines():
            print(line)
          f.close()