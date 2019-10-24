# author Vipul Vaibhaw - vaibhaw.vipul@gmail.com
# Feel free to reach out

# This code is inspired from this talk https://www.youtube.com/watch?v=ggqnxyjaKe4
# Thanks a lot richard sutton - http://incompleteideas.net/

import random
import numpy as np
# np.random.choice(4, 1000, p=[0.1, 0.2, 0.3, 0.4])

actions_to_take = [1, 2]
states = ["A", "B"]

# define global counter for time step

time_step = 0 
initial_state = states[0]

print("\nWelcome to a simulation!")
print("This code is inspired from this talk - https://youtu.be/ggqnxyjaKe4?t=934\n")

print("Actions={1, 2}")

mdp = {"time": time_step, "state": initial_state}

current_state = initial_state


def rewards(amount):
    if amount == "small pos":
        print("\treward: +" + str(random.randint(10, 15)))
    elif amount == "small neg":
        print("\treward: " + str(random.randint(-15, -10)))
    elif amount == "big pos":
        print("\treward: +" + str(random.randint(37, 50)))
    else:
        print("\treward: +" + str(random.randint(0, 5)))


def changeState(currentState, UserInput):
    global current_state
    # if current State is A and user presses 1, come back to A 100% times. small reward.
    if currentState == "A" and userInput == 1:
        current_state = states[0]
        rewards("small pos for A") 
    # if current State is A and user presses 2,
    # 80% chances that it goes to B and 20% that it comes back to A.
    # Small negative reward.
    elif currentState == "A" and userInput == 2:
        current_state = np.random.choice(states, 1, p=[0.2, 0.8])[0]
        if current_state == "A":
            rewards("small pos")
        else:
            rewards("small neg")
    # if current state is B and user presses 1,
    # 80% chances that it goes to A and 20% that it comes back to B.
    # Big reward.
    elif currentState == "B" and userInput == 1:
        current_state = np.random.choice(states, 1, p=[0.8, 0.2])[0]
        if current_state == "B":
            rewards("small neg")
        else:
            rewards("big pos")
    # if current state is B and user presses 1,
    # 80% chances that it goes to A and 20% that it comes back to B.
    # Small reward.
    elif currentState == "B" and userInput == 2:
        current_state = np.random.choice(states, 1, p=[0.8, 0.2])[0]
        if current_state == "A":
            rewards("small pos")
        else:
            rewards("small neg")
    else:
        print("Boo!")


def updateMdp(time_step, current_state):
    global mdp
    mdp = {"time": time_step, "state": current_state}


def printMsg(mdp):
    print("time = "+str(mdp["time"])+", state = "+mdp["state"]+", action = ")


def getGlobals():
    global actions_to_take
    return actions_to_take


if __name__ == "__main__":
    actions_to_take = getGlobals()
    while True:
        printMsg(mdp)
        userInput = int(input())
        if userInput not in actions_to_take:
            print("Invalid action. Please choose one of {}".format(actions_to_take))
            continue
        changeState(current_state, userInput)
        time_step = time_step + 1 
        updateMdp(time_step, current_state)

