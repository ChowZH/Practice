import math

##Task 1
Bob = 9 - 3
Total = Bob * 2

##Task 2
def cylinder_vol(r, h):
    vol = (math.pi*(r**2))*h
    return vol

##Task 3
def cumsum(x):
    y = 0
    for i in range(x):
        i += 1
        y += i
    return y

def mean(x, n):
    y = x/n
    return y

##Task 4
ProfitPerPie = 5 - 2.99

def profit_cal(n, d):
    total_profit = ProfitPerPie*n*d
    return total_profit

## Assignment Task 1

def cylinder_area(r, h):
    area = (math.pi*(r**2)*2) + (2*math.pi*r*h)
    return area

if __name__ == "__main__":
    print ("Answer for task 1 : {}" .format(Total))
    print ("Answer for task 2 : {}" .format(cylinder_vol (5, 1)))
    print ("Answer for task 3 : {}" .format(mean(cumsum(7), 7)))
    print ("Answer for task 4 : {0:.2f}" .format(profit_cal(6, 7)))
    # Assignment Task 1
    print ("Answer for Assignment Task 1: {}" .format(cylinder_area (2, 0.5)))
    # Assisgnment Task 2
    print ("Answer for Assignment Task 2:")
    print ("Sing a song of sixpence,\nA pocket full of rye,\nFour and twenty blackbirds\nBaked in a pie.\n")
    print ("When the pie was opened\nThe birds began to sing—\nWasn't that a dainty dish\nTo set before the king?\n")
    print ("The king was in the counting-house\nCounting out his money,\nThe queen was in the parlor\nEating bread and honey,\n")
    print ("The maid was in the garden\nHanging out the clothes.\nAlong came a blackbird\nAnd snipped off her nose.\n")
    print ("Sing a song of sixpence,\nA pocket full of rye,\nFour and twenty blackbirds\nBaked in a pie.\n")
    print ("When the pie was opened\nThe birds began to sing—\nWasn't that a dainty dish\nTo set before the king?")