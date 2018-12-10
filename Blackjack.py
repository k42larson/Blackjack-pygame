import pygame, sys
import time
from pygame.locals import*
import math
import random
cash = 1000
bet = 0
chipLocs = [(755,555), (665,555), (575,555), (485,555), (755,465), (665,465), (575,465)]
chipVals = [500, 100, 50, 25, 10, 5, 1]
def printMoney():
    pygame.draw.rect(window, (0, 128, 0), [0, 0, 200, 60])
    textsurface = myfont.render('Cash: $' + str(cash), False, (255, 255, 255))
    window.blit(textsurface,(0,0))
    textsurface2 = myfont.render('Bet: $' + str(bet), False, (255, 255, 255))
    window.blit(textsurface2,(0,30))
    pygame.display.update()

def isButtonPressed(x, w=100):
    return pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < x+w and pygame.mouse.get_pos()[1] > 600 and pygame.mouse.get_pos()[1] < 650

def firstMove():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(isButtonPressed(0)):
                    return 1
                elif(isButtonPressed(140)):
                    return 2
                elif(isButtonPressed(280)):
                    return 3
                elif(isButtonPressed(420)):
                    return 4
def posSplitMove():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(isButtonPressed(0)):
                    return 1
                elif(isButtonPressed(140)):
                    return 2
                elif(isButtonPressed(280)):
                    return 3
                elif(isButtonPressed(420)):
                    return 4
                elif(isButtonPressed(560)):
                    return 5
def nextMove():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(isButtonPressed(0)):
                    return 1
                elif(isButtonPressed(140)):
                    return 2
def move():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(isButtonPressed(0)):
                    return 1
                elif(isButtonPressed(140)):
                    return 2
                elif(isButtonPressed(280)):
                    return 3

def pointsTotal(cards):
    aceTotal = 0
    tot = 0
    for c in cards:
        if c == 11:
           tot += 1
           aceTotal += 1
        else:
            tot += c
    i = 0
    done = False
    while i < aceTotal:
        if(tot + 10 <= 21):
            tot += 10
            i = i+1
        else:
            done = True
        if done:
            break
    return tot
def isChosen(a, numsChosen):
    for n in numsChosen:
        if a == n:
            return True
    return False
def randomNum(numsChosen):
    num = random.randint(0, 52*6-1)
    while(isChosen(num, numsChosen)):
        num = random.randint(0, 52*6-1)
    return num

def calcDist(a, b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))

def makeBet(bet, cash):
    betFinalized = 0
    done = False
    button = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                if(button == 1 or button == 3):
                    done = True
                    break
                if done:
                    break
            if done:
                break
        if done:
            break
    i = 0
    while i < 7:
        if(calcDist(pygame.mouse.get_pos(), chipLocs[i]) < 45):
            if(button == 1):
                if(bet + chipVals[i] <= cash):
                    bet += chipVals[i]
            else:
                if(bet - chipVals[i] >= 0):
                    bet -= chipVals[i]
            break
        i += 1
        if i == 7:
            if(isButtonPressed(0, 95)):
               betFinalized = 1
    return bet, betFinalized
            
def printStart(chip500, chip100, chip50, chip25, chip10, chip5, chip1):
    window.fill((0, 128, 0))
    window.blit(pygame.image.load('bj_banner_yellow2.png'), (150,150))
    window.blit(pygame.image.load('big bet.png'), (0, 600))
    window.blit(chip500, (710,510))
    window.blit(chip100, (620,510))
    window.blit(chip50, (530,510))
    window.blit(chip25, (440,510))
    window.blit(chip10, (710,420))
    window.blit(chip5, (620,420))
    window.blit(chip1, (530,420))
    pygame.display.update()
    printMoney()
pygame.init()
green = (0, 128, 0)
deckFile = ['cards/2_of_diamonds.png','cards/2_of_clubs.png','cards/2_of_hearts.png','cards/2_of_spades.png','cards/3_of_diamonds.png','cards/3_of_clubs.png','cards/3_of_hearts.png','cards/3_of_spades.png','cards/4_of_diamonds.png','cards/4_of_clubs.png','cards/4_of_hearts.png','cards/4_of_spades.png','cards/5_of_diamonds.png','cards/5_of_clubs.png','cards/5_of_hearts.png','cards/5_of_spades.png','cards/6_of_diamonds.png','cards/6_of_clubs.png','cards/6_of_hearts.png','cards/6_of_spades.png','cards/7_of_diamonds.png','cards/7_of_clubs.png','cards/7_of_hearts.png','cards/7_of_spades.png','cards/8_of_diamonds.png','cards/8_of_clubs.png','cards/8_of_hearts.png','cards/8_of_spades.png','cards/9_of_diamonds.png','cards/9_of_clubs.png','cards/9_of_hearts.png','cards/9_of_spades.png','cards/10_of_diamonds.png','cards/10_of_clubs.png','cards/10_of_hearts.png','cards/10_of_spades.png','cards/jack_of_diamonds.png','cards/jack_of_clubs.png','cards/jack_of_hearts.png','cards/jack_of_spades.png','cards/queen_of_diamonds.png','cards/queen_of_clubs.png','cards/queen_of_hearts.png','cards/queen_of_spades.png','cards/king_of_diamonds.png','cards/king_of_clubs.png','cards/king_of_hearts.png','cards/king_of_spades.png','cards/ace_of_diamonds.png','cards/ace_of_clubs.png','cards/ace_of_hearts.png','cards/ace_of_spades.png','cards/2_of_diamonds.png','cards/2_of_clubs.png','cards/2_of_hearts.png','cards/2_of_spades.png','cards/3_of_diamonds.png','cards/3_of_clubs.png','cards/3_of_hearts.png','cards/3_of_spades.png','cards/4_of_diamonds.png','cards/4_of_clubs.png','cards/4_of_hearts.png','cards/4_of_spades.png','cards/5_of_diamonds.png','cards/5_of_clubs.png','cards/5_of_hearts.png','cards/5_of_spades.png','cards/6_of_diamonds.png','cards/6_of_clubs.png','cards/6_of_hearts.png','cards/6_of_spades.png','cards/7_of_diamonds.png','cards/7_of_clubs.png','cards/7_of_hearts.png','cards/7_of_spades.png','cards/8_of_diamonds.png','cards/8_of_clubs.png','cards/8_of_hearts.png','cards/8_of_spades.png','cards/9_of_diamonds.png','cards/9_of_clubs.png','cards/9_of_hearts.png','cards/9_of_spades.png','cards/10_of_diamonds.png','cards/10_of_clubs.png','cards/10_of_hearts.png','cards/10_of_spades.png','cards/jack_of_diamonds.png','cards/jack_of_clubs.png','cards/jack_of_hearts.png','cards/jack_of_spades.png','cards/queen_of_diamonds.png','cards/queen_of_clubs.png','cards/queen_of_hearts.png','cards/queen_of_spades.png','cards/king_of_diamonds.png','cards/king_of_clubs.png','cards/king_of_hearts.png','cards/king_of_spades.png','cards/ace_of_diamonds.png','cards/ace_of_clubs.png','cards/ace_of_hearts.png','cards/ace_of_spades.png','cards/2_of_diamonds.png','cards/2_of_clubs.png','cards/2_of_hearts.png','cards/2_of_spades.png','cards/3_of_diamonds.png','cards/3_of_clubs.png','cards/3_of_hearts.png','cards/3_of_spades.png','cards/4_of_diamonds.png','cards/4_of_clubs.png','cards/4_of_hearts.png','cards/4_of_spades.png','cards/5_of_diamonds.png','cards/5_of_clubs.png','cards/5_of_hearts.png','cards/5_of_spades.png','cards/6_of_diamonds.png','cards/6_of_clubs.png','cards/6_of_hearts.png','cards/6_of_spades.png','cards/7_of_diamonds.png','cards/7_of_clubs.png','cards/7_of_hearts.png','cards/7_of_spades.png','cards/8_of_diamonds.png','cards/8_of_clubs.png','cards/8_of_hearts.png','cards/8_of_spades.png','cards/9_of_diamonds.png','cards/9_of_clubs.png','cards/9_of_hearts.png','cards/9_of_spades.png','cards/10_of_diamonds.png','cards/10_of_clubs.png','cards/10_of_hearts.png','cards/10_of_spades.png','cards/jack_of_diamonds.png','cards/jack_of_clubs.png','cards/jack_of_hearts.png','cards/jack_of_spades.png','cards/queen_of_diamonds.png','cards/queen_of_clubs.png','cards/queen_of_hearts.png','cards/queen_of_spades.png','cards/king_of_diamonds.png','cards/king_of_clubs.png','cards/king_of_hearts.png','cards/king_of_spades.png','cards/ace_of_diamonds.png','cards/ace_of_clubs.png','cards/ace_of_hearts.png','cards/ace_of_spades.png','cards/2_of_diamonds.png','cards/2_of_clubs.png','cards/2_of_hearts.png','cards/2_of_spades.png','cards/3_of_diamonds.png','cards/3_of_clubs.png','cards/3_of_hearts.png','cards/3_of_spades.png','cards/4_of_diamonds.png','cards/4_of_clubs.png','cards/4_of_hearts.png','cards/4_of_spades.png','cards/5_of_diamonds.png','cards/5_of_clubs.png','cards/5_of_hearts.png','cards/5_of_spades.png','cards/6_of_diamonds.png','cards/6_of_clubs.png','cards/6_of_hearts.png','cards/6_of_spades.png','cards/7_of_diamonds.png','cards/7_of_clubs.png','cards/7_of_hearts.png','cards/7_of_spades.png','cards/8_of_diamonds.png','cards/8_of_clubs.png','cards/8_of_hearts.png','cards/8_of_spades.png','cards/9_of_diamonds.png','cards/9_of_clubs.png','cards/9_of_hearts.png','cards/9_of_spades.png','cards/10_of_diamonds.png','cards/10_of_clubs.png','cards/10_of_hearts.png','cards/10_of_spades.png','cards/jack_of_diamonds.png','cards/jack_of_clubs.png','cards/jack_of_hearts.png','cards/jack_of_spades.png','cards/queen_of_diamonds.png','cards/queen_of_clubs.png','cards/queen_of_hearts.png','cards/queen_of_spades.png','cards/king_of_diamonds.png','cards/king_of_clubs.png','cards/king_of_hearts.png','cards/king_of_spades.png','cards/ace_of_diamonds.png','cards/ace_of_clubs.png','cards/ace_of_hearts.png','cards/ace_of_spades.png','cards/2_of_diamonds.png','cards/2_of_clubs.png','cards/2_of_hearts.png','cards/2_of_spades.png','cards/3_of_diamonds.png','cards/3_of_clubs.png','cards/3_of_hearts.png','cards/3_of_spades.png','cards/4_of_diamonds.png','cards/4_of_clubs.png','cards/4_of_hearts.png','cards/4_of_spades.png','cards/5_of_diamonds.png','cards/5_of_clubs.png','cards/5_of_hearts.png','cards/5_of_spades.png','cards/6_of_diamonds.png','cards/6_of_clubs.png','cards/6_of_hearts.png','cards/6_of_spades.png','cards/7_of_diamonds.png','cards/7_of_clubs.png','cards/7_of_hearts.png','cards/7_of_spades.png','cards/8_of_diamonds.png','cards/8_of_clubs.png','cards/8_of_hearts.png','cards/8_of_spades.png','cards/9_of_diamonds.png','cards/9_of_clubs.png','cards/9_of_hearts.png','cards/9_of_spades.png','cards/10_of_diamonds.png','cards/10_of_clubs.png','cards/10_of_hearts.png','cards/10_of_spades.png','cards/jack_of_diamonds.png','cards/jack_of_clubs.png','cards/jack_of_hearts.png','cards/jack_of_spades.png','cards/queen_of_diamonds.png','cards/queen_of_clubs.png','cards/queen_of_hearts.png','cards/queen_of_spades.png','cards/king_of_diamonds.png','cards/king_of_clubs.png','cards/king_of_hearts.png','cards/king_of_spades.png','cards/ace_of_diamonds.png','cards/ace_of_clubs.png','cards/ace_of_hearts.png','cards/ace_of_spades.png','cards/2_of_diamonds.png','cards/2_of_clubs.png','cards/2_of_hearts.png','cards/2_of_spades.png','cards/3_of_diamonds.png','cards/3_of_clubs.png','cards/3_of_hearts.png','cards/3_of_spades.png','cards/4_of_diamonds.png','cards/4_of_clubs.png','cards/4_of_hearts.png','cards/4_of_spades.png','cards/5_of_diamonds.png','cards/5_of_clubs.png','cards/5_of_hearts.png','cards/5_of_spades.png','cards/6_of_diamonds.png','cards/6_of_clubs.png','cards/6_of_hearts.png','cards/6_of_spades.png','cards/7_of_diamonds.png','cards/7_of_clubs.png','cards/7_of_hearts.png','cards/7_of_spades.png','cards/8_of_diamonds.png','cards/8_of_clubs.png','cards/8_of_hearts.png','cards/8_of_spades.png','cards/9_of_diamonds.png','cards/9_of_clubs.png','cards/9_of_hearts.png','cards/9_of_spades.png','cards/10_of_diamonds.png','cards/10_of_clubs.png','cards/10_of_hearts.png','cards/10_of_spades.png','cards/jack_of_diamonds.png','cards/jack_of_clubs.png','cards/jack_of_hearts.png','cards/jack_of_spades.png','cards/queen_of_diamonds.png','cards/queen_of_clubs.png','cards/queen_of_hearts.png','cards/queen_of_spades.png','cards/king_of_diamonds.png','cards/king_of_clubs.png','cards/king_of_hearts.png','cards/king_of_spades.png','cards/ace_of_diamonds.png','cards/ace_of_clubs.png','cards/ace_of_hearts.png','cards/ace_of_spades.png']
deckValues = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]
window = pygame.display.set_mode((800, 650))
pygame.display.set_caption("Blackjack")
chip500 = pygame.image.load('pokerchips/chip500.png')
chip500 = pygame.transform.scale(chip500, (90, 90))
chip100 = pygame.image.load('pokerchips/chip100.png')
chip100 = pygame.transform.scale(chip100, (90, 90))
chip50 = pygame.image.load('pokerchips/chip50.png')
chip50 = pygame.transform.scale(chip50, (90, 90))
chip25 = pygame.image.load('pokerchips/chip25.png')
chip25 = pygame.transform.scale(chip25, (90, 90))
chip10 = pygame.image.load('pokerchips/chip10.png')
chip10 = pygame.transform.scale(chip10, (90, 90))
chip5 = pygame.image.load('pokerchips/chip5.png')
chip5 = pygame.transform.scale(chip5, (90, 90))
chip1 = pygame.image.load('pokerchips/chip1.png')
chip1 = pygame.transform.scale(chip1, (90, 90))
myfont = pygame.font.SysFont('Comic Sans MS', 25)
quitb = pygame.image.load('quit.png')
quitb = pygame.transform.scale(quitb , (100, 50))
printStart(chip500, chip100, chip50, chip25, chip10, chip5, chip1)
while True:
    numsChosen = []
    dealervalue = 0
    playervalue = 0
    dealercards = []
    playercards = []
    betFinalized = 0
    window.blit(pygame.image.load('betinstructions.png'), (575, 300))
    pygame.display.update()
    print(cash)
    while betFinalized == 0 or bet == 0:
        bet, betFinalized = makeBet(bet, cash)
        printMoney()
    pygame.draw.rect(window, (0, 128, 0), [575, 300, 200, 100])
    window.blit(pygame.image.load('cards/cardback.png'), (350, 50))
    numsChosen.append(randomNum(numsChosen))
    dealercards.append(deckValues[numsChosen[0]])
    pygame.display.update()
    time.sleep(.5)
    numsChosen.append(randomNum(numsChosen))
    dealercards.append(deckValues[numsChosen[1]])
    window.blit(pygame.image.load(deckFile[numsChosen[1]]), (370, 70))
    pygame.display.update()
    time.sleep(.5)
    numsChosen.append(randomNum(numsChosen))
    playercards.append(deckValues[numsChosen[2]])
    window.blit(pygame.image.load(deckFile[numsChosen[2]]), (100, 300))
    pygame.display.update()
    time.sleep(.5)
    numsChosen.append(randomNum(numsChosen))
    playercards.append(deckValues[numsChosen[3]])
    window.blit(pygame.image.load(deckFile[numsChosen[3]]), (120, 320))
    pygame.display.update()
    playervalue = pointsTotal(playercards)
    textsurface2 = myfont.render(str(playervalue), False, (255, 255, 255))
    window.blit(textsurface2,(60,350))
    pygame.display.update()
    cardsUsed = 3
    if(playervalue == 21):
        blackjack = pygame.image.load('Blackjack.png')
        window.blit(blackjack, (25, 250))
        cash += bet*1.5
        cash = round(cash, 0)
        bet = 0
        printMoney()
    else:
        window.blit(pygame.image.load('hit.png'), (0, 600))
        window.blit(pygame.image.load('stand.png'), (140, 600))
        window.blit(pygame.image.load('surrender.png'), (280, 600))
        pygame.display.update()
        m = 0
        if(bet*2 <= cash):
            window.blit(pygame.image.load('doubledown.png'), (420, 600))
            pygame.display.update()
            if(playercards[0] == playercards[1]):
                Split = pygame.image.load('Split.png')
                window.blit(pygame.transform.scale(Split, (100, 50)), (560, 600))
                pygame.display.update()
                m = posSplitMove()
            else:
                m = firstMove()
        else:
            m = move()
        if(m == 5):
            bet = bet*2
            printMoney()
            pygame.draw.rect(window, (0, 128, 0), [100, 300, 100, 150])
            window.blit(pygame.image.load('arrow.png'), (125, 275))
            window.blit(pygame.image.load(deckFile[numsChosen[2]]), (100, 300))
            window.blit(pygame.image.load(deckFile[numsChosen[3]]), (250, 300))
            playercards1 = []
            playercards2 = []
            playercards1.append(deckValues[numsChosen[2]])
            playercards2.append(deckValues[numsChosen[3]])
            cardsUsed += 1
            numsChosen.append(randomNum(numsChosen))
            playercards1.append(deckValues[numsChosen[cardsUsed]])
            window.blit(pygame.image.load(deckFile[numsChosen[cardsUsed]]), (120, 320))
            playervalue1 = pointsTotal(playercards1)
            pygame.draw.rect(window, (0, 128, 0), [280, 600, 380, 50])
            pygame.draw.rect(window, (0, 128, 0), [60, 350, 40, 30])
            textsurface2 = myfont.render(str(playervalue1), False, (255, 255, 255))
            window.blit(textsurface2,(60,350))
            pygame.display.update()
            m = nextMove()
            while m == 1:
                cardsUsed += 1
                numsChosen.append(randomNum(numsChosen))
                newCard = pygame.image.load(deckFile[numsChosen[cardsUsed]])
                window.blit(newCard, (100+(len(playercards1))*20, 300+(len(playercards1))*20))
                playercards1.append(deckValues[numsChosen[cardsUsed]])
                playervalue1 = pointsTotal(playercards1)
                pygame.draw.rect(window, (0, 128, 0), [60, 350, 40, 30])
                textsurface2 = myfont.render(str(playervalue1), False, (255, 255, 255))
                window.blit(textsurface2,(60,350))
                pygame.display.update()
                if(playervalue1 >= 21):
                    break
                m = nextMove()
            cardsUsed += 1
            numsChosen.append(randomNum(numsChosen))
            playercards2.append(deckValues[numsChosen[cardsUsed]])
            window.blit(pygame.image.load(deckFile[numsChosen[cardsUsed]]), (270, 320))
            playervalue2 = pointsTotal(playercards2)
            textsurface2 = myfont.render(str(playervalue2), False, (255, 255, 255))
            window.blit(textsurface2,(210,300))
            pygame.draw.rect(window, (0, 128, 0), [125, 275, 25, 25])
            window.blit(pygame.image.load('arrow.png'), (275, 275))
            pygame.display.update()
            m = nextMove()
            while m == 1:
                cardsUsed += 1
                numsChosen.append(randomNum(numsChosen))
                newCard = pygame.image.load(deckFile[numsChosen[cardsUsed]])
                window.blit(newCard, (250+(len(playercards2))*20, 300+(len(playercards2))*20))
                playercards2.append(deckValues[numsChosen[cardsUsed]])
                playervalue2 = pointsTotal(playercards2)
                pygame.draw.rect(window, (0, 128, 0), [210, 300, 40, 30])
                textsurface2 = myfont.render(str(playervalue2), False, (255, 255, 255))
                window.blit(textsurface2,(210,300))
                pygame.display.update()
                if(playervalue2 >= 21):
                    break
                m = nextMove()
            if(playervalue1 == 21 and playervalue2 == 21):
                cash += bet
                bet = 0
                printMoney()
            else:
                dealervalue = pointsTotal(dealercards)
                window.blit(pygame.image.load(deckFile[numsChosen[0]]), (350, 50))
                window.blit(pygame.image.load(deckFile[numsChosen[1]]), (370, 70))
                pygame.draw.rect(window, (0, 128, 0), [350, 0, 50, 50])
                textsurface2 = myfont.render(str(dealervalue), False, (255, 255, 255))
                window.blit(textsurface2,(350,0))
                pygame.display.update()
                time.sleep(.5)
                while dealervalue <= 16:
                    cardsUsed += 1
                    numsChosen.append(randomNum(numsChosen))
                    dealercards.append(deckValues[numsChosen[cardsUsed]])
                    window.blit(pygame.image.load(deckFile[numsChosen[cardsUsed]]), (330+len(dealercards)*20, 30+len(dealercards)*20))
                    dealervalue = pointsTotal(dealercards)
                    pygame.draw.rect(window, (0, 128, 0), [350, 0, 50, 50])
                    textsurface2 = myfont.render(str(dealervalue), False, (255, 255, 255))
                    window.blit(textsurface2,(350,0))
                    pygame.display.update()
                    time.sleep(.5)
            if(playervalue1 > 21):
                window.blit(pygame.image.load('busted.png'), (25, 250))
                cash -= bet/2
                bet = bet/2
                printMoney()
            elif(playervalue1 > dealervalue or dealervalue > 21):
                window.blit(pygame.image.load('winner.png'), (25, 250))
                cash += bet/2
                bet = bet/2
                printMoney()
            elif(playervalue1 < dealervalue):
                window.blit(pygame.image.load('taketheL.png'), (25, 250))
                cash -= bet/2
                bet = bet/2
                printMoney()
            else:
                window.blit(pygame.image.load('push.png'), (25, 250))
                bet = bet/2
                printMoney()
            if(playervalue2 > 21):
                window.blit(pygame.image.load('busted.png'), (400, 350))
                cash -= bet
                bet = 0
                printMoney()
            elif(playervalue2 > dealervalue or dealervalue > 21):
                window.blit(pygame.image.load('winner.png'), (400, 350))
                cash += bet
                bet = 0
                printMoney()
            elif(playervalue2 < dealervalue):
                window.blit(pygame.image.load('taketheL.png'), (400, 350))
                cash -= bet
                bet = 0
                printMoney()
            else:
                window.blit(pygame.image.load('push.png'), (400, 350))
                bet = 0
                printMoney()
            m = 0
            playervalue = playervalue1
        elif(m == 4):
            bet = bet*2
            printMoney()
            cardsUsed += 1
            numsChosen.append(randomNum(numsChosen))
            newCard = pygame.image.load(deckFile[numsChosen[cardsUsed]])
            window.blit(pygame.transform.rotate(newCard, 90), (140, 340))
            playercards.append(deckValues[numsChosen[cardsUsed]])
            playervalue = pointsTotal(playercards)
            pygame.draw.rect(window, (0, 128, 0), [60, 350, 40, 30])
            textsurface2 = myfont.render(str(playervalue), False, (255, 255, 255))
            window.blit(textsurface2,(60,350))
            pygame.display.update()
        elif(m == 3):
            cash -= bet*.5
            cash = round(cash, 0)
            bet = 0
            printMoney()
            m = 0
        while m == 1:
            pygame.draw.rect(window, (0, 128, 0), [280, 600, 380, 50])
            cardsUsed += 1
            numsChosen.append(randomNum(numsChosen))
            newCard = pygame.image.load(deckFile[numsChosen[cardsUsed]])
            window.blit(newCard, (140+(cardsUsed-4)*20, 340+(cardsUsed-4)*20))
            playercards.append(deckValues[numsChosen[cardsUsed]])
            playervalue = pointsTotal(playercards)
            pygame.draw.rect(window, (0, 128, 0), [60, 350, 40, 30])
            textsurface2 = myfont.render(str(playervalue), False, (255, 255, 255))
            window.blit(textsurface2,(60,350))
            pygame.display.update()
            if(playervalue >= 21):
                break
            m = nextMove()
        if(playervalue == 21):
            cash += bet
            bet = 0
            printMoney()
        elif(playervalue < 21 and m > 0):
            dealervalue = pointsTotal(dealercards)
            window.blit(pygame.image.load(deckFile[numsChosen[0]]), (350, 50))
            window.blit(pygame.image.load(deckFile[numsChosen[1]]), (370, 70))
            pygame.draw.rect(window, (0, 128, 0), [350, 0, 50, 50])
            textsurface2 = myfont.render(str(dealervalue), False, (255, 255, 255))
            window.blit(textsurface2,(350,0))
            pygame.display.update()
            time.sleep(.5)
            while dealervalue <= 16:
                cardsUsed += 1
                numsChosen.append(randomNum(numsChosen))
                dealercards.append(deckValues[numsChosen[cardsUsed]])
                window.blit(pygame.image.load(deckFile[numsChosen[cardsUsed]]), (330+len(dealercards)*20, 30+len(dealercards)*20))
                dealervalue = pointsTotal(dealercards)
                pygame.draw.rect(window, (0, 128, 0), [350, 0, 50, 50])
                textsurface2 = myfont.render(str(dealervalue), False, (255, 255, 255))
                window.blit(textsurface2,(350,0))
                pygame.display.update()
                time.sleep(.5)
        if(playervalue > 21):
            window.blit(pygame.image.load('busted.png'), (25, 250))
            cash -= bet
            bet = 0
            printMoney()
        elif(dealervalue == 0):
            window.blit(pygame.transform.scale(pygame.image.load('surrendered.png'), (100, 50)), (25, 250))
        elif(playervalue > dealervalue or dealervalue > 21):
            window.blit(pygame.image.load('winner.png'), (25, 250))
            cash += bet
            bet = 0
            printMoney()
        elif(playervalue < dealervalue):
            window.blit(pygame.image.load('taketheL.png'), (25, 250))
            cash -= bet
            bet = 0
            printMoney()
        else:
            window.blit(pygame.image.load('push.png'), (25, 250))
            bet = 0
            printMoney()
    pygame.draw.rect(window, (0, 128, 0), [0, 600, 800, 50])
    window.blit(quitb, (700, 600))
    window.blit(pygame.image.load('Cont.jpg'), (600, 600))
    pygame.display.update()
    cont = False
    if(cash == 0):
        time.sleep(2)
        window.fill(green)
        BB = pygame.image.load('brokeass.png')
        window.blit(pygame.transform.scale(BB, (400, 200)), (200, 200))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(isButtonPressed(700)):
                    pygame.quit()
                elif(isButtonPressed(600)):
                    cont = True
                if(cont == True):
                    break
            if(cont == True):
                break
        if(cont == True):
            break
    printStart(chip500, chip100, chip50, chip25, chip10, chip5, chip1)
    

