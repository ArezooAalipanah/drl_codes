def main():
    P_FL = {
        0: {  # (1) The outer dictionary keys are the states.
            0: [(1/3, 0, 0.0, False),(1/3, 0, 0.0, False),(1/3, 4, 0.0, False)],  # (2) The inner dictionary keys are the actions.
            1: [(1/3, 0, 0.0, False),(1/3, 0, 0.0, False),(1/3, 1, 0.0, False)],  # (3) The value of the inner dictionary is a list with all possible transitions
            2: [(1/3, 0, 0.0, False),(1/3, 4, 0.0, False),(1/3, 2, 0.0, False)],
            3: [(1/3, 0, 0.0, False),(1/3, 0, 0.0, False),(1/3, 2, 0.0, False)]
        },
        1:{}
    }
    print(P_FL)

if __name__ == '__main__':
    main()