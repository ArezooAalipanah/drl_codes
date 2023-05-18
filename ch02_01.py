import gym
# The Bandit Walk MDP
def main():
    """
    (4) The transition tuples have four values:
    the probability of that transition, the next state, the reward, and a flag indicating whether the next state is terminal.
    """
    P_BW = {
        0: { #(1) The outer dictionary keys are the states.
            0: [(1.0, 0, 0.0, True)], # (2) The inner dictionary keys are the actions.
            1: [(1.0, 0, 0.0, True)]  #(3) The value of the inner dictionary is a list with all possible transitions
        },
        1: {
            0: [(1.0, 0, 0.0, True)],
            1: [(1.0, 2, 1.0, True)] # with a 1 transition you go to state 2 and receive 1 reward and it would be over
        },
        2: {
            0: [(1.0, 2, 0.0, True)],
            1: [(1.0, 2, 0.0, True)]
        }
    }

    P_SBW = {
        0: {  # (1) The outer dictionary keys are the states.
            0: [(1.0, 0, 0.0, True)],  # (2) The inner dictionary keys are the actions.
            1: [(1.0, 0, 0.0, True)]  # (3) The value of the inner dictionary is a list with all possible transitions
        },
        1: {
            0: [(0.8, 0, 0.0, True), (0.2, 2, 1.0, True)],
            1: [(0.8, 2, 1.0, True), (0.2, 0, 0.0, True)]
        },
        2: {
            0: [(1.0, 2, 0.0, True)],
            1: [(1.0, 2, 0.0, True)]
        }
    }

    print(P_SBW)
    print(P_BW)






if __name__ == '__main__':
    main()