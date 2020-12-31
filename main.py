"""
This program  presents all the solutions possible in the game of 24 using cards as numbers

Programmed by: Darren Wu December 2020
"""


# Getting cards from user
card_string = input("Enter the 4 cards separated by spaces(e.g. 1 4 5 6): ")
# Splits input from user into a 4 item int array
cards = [int(i) for i in card_string.split() if i.isdigit()]


# Function to add, subtract, multiply or divide cards
# Returns a array with the two cards combined
def combine(array, index1, index2, function):
    temp = []
    for i in array:
        temp.append(i)
    if(function == 0):
        temp[index1] = temp[index1] + temp[index2]
        temp[index2] = None
    
    if(function == 1):
        temp[index1] = temp[index1] - temp[index2]
        temp[index2] = None
    
    if(function == 2):
        temp[index1] = temp[index1] * temp[index2]
        temp[index2] = None
    
    if(function == 3):
        temp[index1] = temp[index1] / temp[index2]
        temp[index2] = None
    
    ans = []
    for i in range(len(temp)):
        if(temp[i] != None):
            ans.append(temp[i])
    return ans

functions = ['+','-','*','/']
is24 = False
cards1 = []
cards2 = []
ans = []
correct = []
count = 0

for startingCard in range(4):
    for secondCard in range(0, len(cards)):
        if(startingCard != secondCard):
            if(startingCard < secondCard):
                # All 4 math operators if starting card is to the left of the second card in the array
                for firstStep in range(4):
                    if(not(cards[secondCard] == 0 and firstStep == 3)):
                        cards1 = combine(cards, startingCard, secondCard, firstStep)
                        for startingCard2 in range(3):
                                for secondCard2 in range(0, len(cards1)):
                                    if(startingCard2 != secondCard2):
                                        if(startingCard2 < secondCard2):
                                            # All 4 math operators if starting card is to the left of the second card in the array
                                            for secondStep in range(4):
                                                if(not(cards1[secondCard2] == 0 and secondStep == 3)):
                                                    cards2 = combine(cards1, startingCard2, secondCard2, secondStep)
                                                    # All 4 math operators if starting card is to the left of the second card in the array
                                                    for thirdStep in range(4):
                                                        if(not(cards2[1] == 0 and thirdStep == 3)):
                                                            ans = combine(cards2, 0, 1, thirdStep)
                                                            # Used abs() instead of == in case answer is 23.999999
                                                            if (abs(ans[0] - 24) <= 0.01):
                                                                is24 =True
                                                                count += 1
                                                                if(not (cards in correct)):
                                                                    correct.append(cards)
                                                                print('Solution Found!')
                                                                print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                                print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                                print('Third Step: ' + str(cards2[0]) + ' ' + functions[thirdStep] + ' '+ str(cards2[1]))
                                                    # Subtracts and divides if starting card is to the right of second card
                                                    for thirdStep in range(1,4,2):
                                                        if(not(cards2[0] == 0 and thirdStep == 3)):
                                                            ans = combine(cards2, 1, 0, thirdStep)
                                                            if (abs(ans[0] - 24) <= 0.01):
                                                                is24 =True
                                                                count += 1
                                                                if(not (cards in correct)):
                                                                    correct.append(cards)
                                                                print('Solution Found!')
                                                                print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                                print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                                print('Third Step: ' + str(cards2[1]) + ' ' + functions[thirdStep] + ' '+ str(cards2[0]))
                                        else:
                                            # Subtracts and divides if starting card is to the right of second card
                                            for secondStep in range(1,4,2):
                                                if(not(cards1[secondCard2] == 0 and secondStep == 3)):
                                                    cards2 = combine(cards1, startingCard2, secondCard2, secondStep)
                                                    # All 4 math operators if starting card is to the left of the second card in the array
                                                    for thirdStep in range(4):
                                                        if(not(cards2[1] == 0 and thirdStep == 3)):
                                                            ans = combine(cards2, 0, 1, thirdStep)
                                                            if (abs(ans[0] - 24) <= 0.01):
                                                                is24 =True
                                                                count += 1
                                                                if(not (cards in correct)):
                                                                    correct.append(cards)
                                                                print('Solution Found!')
                                                                print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                                print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                                print('Third Step: ' + str(cards2[0]) + ' ' + functions[thirdStep] + ' '+ str(cards2[1]))
                                                    # Subtracts and divides if starting card is to the right of second card
                                                    for thirdStep in range(1,4,2):
                                                        if(not(cards2[0] == 0 and thirdStep == 3)):
                                                            ans = combine(cards2, 1, 0, thirdStep)
                                                            if (abs(ans[0] - 24) <= 0.01):
                                                                is24 =True
                                                                count += 1
                                                                if(not (cards in correct)):
                                                                    correct.append(cards)
                                                                print('Solution Found!')
                                                                print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                                print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                                print('Third Step: ' + str(cards2[1]) + ' ' + functions[thirdStep] + ' '+ str(cards2[0]))
            else:
                # Subtracts and divides if starting card is to the right of second card
                for firstStep in range(1,4,2):
                    if(not(cards[secondCard] == 0 and firstStep == 3)):
                        cards1 = combine(cards, startingCard, secondCard, firstStep)
                    for startingCard2 in range(3):
                        if(startingCard2 == 0):
                            for secondCard2 in range(0, len(cards1)):
                                if(startingCard2 != secondCard2):
                                    if(startingCard2 < secondCard2):
                                        # All 4 math operators if starting card is to the left of the second card in the array
                                        for secondStep in range(4):
                                            if(not(cards1[secondCard2] == 0 and secondStep == 3)):
                                                cards2 = combine(cards1, startingCard2, secondCard2, secondStep)
                                                # All 4 math operators if starting card is to the left of the second card in the array
                                                for thirdStep in range(4):
                                                    if(not(cards2[1] == 0 and thirdStep == 3)):
                                                            ans = combine(cards2, 0, 1, thirdStep)
                                                            if (abs(ans[0] - 24) <= 0.01):
                                                                is24 =True
                                                                count += 1
                                                                if(not (cards in correct)):
                                                                    correct.append(cards)
                                                                print('Solution Found!')
                                                                print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                                print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                                print('Third Step: ' + str(cards2[0]) + ' ' + functions[thirdStep] + ' '+ str(cards2[1]))
                                                # Subtracts and divides if starting card is to the right of second card
                                                for thirdStep in range(1,4,2):
                                                    if(not(cards2[0] == 0 and thirdStep == 3)):
                                                        ans = combine(cards2, 1, 0, thirdStep)
                                                        if (abs(ans[0] - 24) <= 0.01):
                                                            is24 =True
                                                            count += 1
                                                            if(not (cards in correct)):
                                                                correct.append(cards)
                                                            print('Solution Found!')
                                                            print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                            print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                            print('Third Step: ' + str(cards2[1]) + ' ' + functions[thirdStep] + ' '+ str(cards2[0]))
                                    else:
                                        # Subtracts and divides if starting card is to the right of second card
                                        for secondStep in range(1,4,2):
                                            if(not(cards1[secondCard2] == 0 and secondStep == 3)):
                                                cards2 = combine(cards1, startingCard2, secondCard2, secondStep)
                                                # All 4 math operators if starting card is to the left of the second card in the array
                                                for thirdStep in range(4):
                                                    if(not(cards2[1] == 0 and thirdStep == 3)):
                                                            ans = combine(cards2, 0, 1, thirdStep)
                                                            if (abs(ans[0] - 24) <= 0.01):
                                                                is24 =True
                                                                count += 1
                                                                if(not (cards in correct)):
                                                                    correct.append(cards)
                                                                print('Solution Found!')
                                                                print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                                print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                                print('Third Step: ' + str(cards2[0]) + ' ' + functions[thirdStep] + ' '+ str(cards2[1]))
                                                # Subtracts and divides if starting card is to the right of second card
                                                for thirdStep in range(1,4,2):
                                                    if(not(cards2[0] == 0 and thirdStep == 3)):
                                                        ans = combine(cards2, 1, 0, thirdStep)
                                                        if (abs(ans[0] - 24) <= 0.01):
                                                            is24 =True
                                                            count += 1
                                                            if(not (cards in correct)):
                                                                correct.append(cards)
                                                            print('Solution Found!')
                                                            print('First Step: ' + str(cards[startingCard]) + functions[firstStep] + str(cards[secondCard]))
                                                            print('Second Step: ' + str(cards1[startingCard2]) + functions[secondStep] + str(cards1[secondCard2]))
                                                            print('Third Step: ' + str(cards2[1]) + ' ' + functions[thirdStep] + ' '+ str(cards2[0]))

if(is24):
    print('In total I found ' + str(count) + ' solutions!')
else:
    print('No solutions found.')