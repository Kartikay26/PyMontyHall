import random, pylab, numpy as np

n = int(input("Enter number of simulations to run: "))

i = 0
switchwin = 0
stickwin = 0
stickwinlist = []
switchwinlist = []

while i < n:

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Simulation number: " + str(i+1))

    winningdoor = random.randint(1,3)
    doorchosen = random.randint(1,3)
    
    # monty opens a door, and shows a goat inside it
    # monty cannot open the winning door, and neither the door we chose
    
    choices_with_monty = [1,2,3]
    choices_with_monty.remove(doorchosen)
    if winningdoor in choices_with_monty: choices_with_monty.remove(winningdoor)
    monty_opens = random.choice(choices_with_monty)

    # choice #1: we stick

    if winningdoor == doorchosen:
        stickwin += 1

    # choice #2: we switch

    doorchosen = (1+2+3) - monty_opens - doorchosen

    if winningdoor == doorchosen:
        switchwin += 1

    stickwinlist.append(stickwin)
    switchwinlist.append(switchwin)

    print("Score so far: " if (i!=n-1) else "Final Score")
    print("Times won by sticking to initial choice: " + str(stickwin))
    print("Times won by switching choice: " + str(switchwin))
    #pylab.pause(0.05)

    i+=1

pylab.title("Comparison of switch vs stick strategy for Monty Hall Problem over " + str(n) + " trials")
pylab.plot(np.arange(0,n), stickwinlist, 'b', label='Stick')
pylab.plot(np.arange(0,n), switchwinlist, 'g', label='Switch')
pylab.legend(loc='best')
pylab.xlabel("Number of wins")
pylab.ylabel("Number of trials")
pylab.show()
