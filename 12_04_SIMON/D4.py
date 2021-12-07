#from numpy import True_
import pandas as pd
from collections import Counter

with open('D4/D4inp.txt') as inp:
    inpread = inp.readlines()

#get called numbers
bingNums = []

for x in inpread[0][:-1].split(','):
    bingNums.append(int(x))
####
#process a line of card
def lineProcess(line):
    procStr =[]
    newLine = line.rstrip().split(' ') 
    for x in newLine:
        if x.isnumeric():
            procStr.append(int(x))
    return procStr
#create individual cards
def createCards(inputF):
    cardHolder = []
    tempCard = []
    for line in inputF:
        if line == '\n':
            cardHolder.append(tempCard)
            tempCard=[]
        else:
            tempCard.append(lineProcess(line))
    return cardHolder

#######
#create card class to keep track of game
class playingCard:
    myCard = []
    markedIndx = ''
    numbersTScore = []
    currentScore = 0 
    winner = False
    finalScore = 0
    winningNum = 777
    finalNumsToScore = []
    calls = 0
    callstoWin = 0

    def __init__(self, card) -> None:
        self.myCard = card
        self.updateNumsToScore()
    
    def printCard(self):
        print(self.myCard)
    
    def printnumbersTScore(self):
        print(self.numbersTScore)
    
    def printMarks(self):
        print(self.markedIndx)
    
    def printCurScr(self):
        print(self.currentScore)

    def updateNumsToScore(self):
        temp=[]
        for row in self.myCard:
            for entry in row:
                temp.append(entry)
        self.numbersTScore = temp

    def calcCurrentScore(self, playedNum):
        self.currentScore = sum(self.numbersTScore) * playedNum

    def checkIfWon(self):
        x = Counter(self.markedIndx)
        holder = 'False'
        for thing in x:
            if x[thing] == 5:
                 holder = True
        return holder
    
    def updateScrNms(self, called):
        temp = []
        for x in self.numbersTScore:
            if x != called:
                temp.append(x)
        self.numbersTScore = temp


    def stampNumber(self, called):
        self.calls+=1
        rw = 0
        for row in self.myCard:
            col = 0
            for entry in row:
                #print(rw, col, entry)  
                if entry == called:
                    #print(chr(rw+65)+str(col))
                    self.markedIndx += chr(rw+65)+str(col)
                    self.updateScrNms(called)
                    self.calcCurrentScore(called)
                    #print(self.winner)
                    if self.checkIfWon() == True:
                        if self.winner == False:
                            #print('here')
                            self.callstoWin = self.calls
                            #print ('Winner with a score of', self.currentScore)
                            self.finalScore = self.currentScore
                            self.winner = True
                            self.winningNum = called
                            self.finalNumsToScore = self.numbersTScore
                col+=1
            rw+=1

#take input and create a table(list) of Bingo Cards
bingInput = inpread[2:]
cards = createCards(bingInput)
gramsTable= []
for x in cards:
    holder = playingCard(x)
    gramsTable.append(holder)

#run all entries through bingo cards
for x in bingNums:
    for card in gramsTable:
        card.stampNumber(x)

#find winner and final score part 1   
temp = 100
currentWinner = 0
for card in gramsTable:
    if card.callstoWin < temp:
        temp = card.callstoWin
        currentWinner = card.finalScore

temp2 =0
currentWinner2 = 0
for card in gramsTable:
    if card.callstoWin > temp2:
        temp2 = card.callstoWin
        currentWinner2 = card.finalScore


print("the winnning score for part one was:", currentWinner)
print("the wiinning score for part 2 is:", currentWinner2)
#58374 is answer
