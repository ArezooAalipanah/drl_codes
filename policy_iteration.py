import numpy as np
import policy_improvement
import policy_evaluation

def policy_iteration(P, gamma = 1.0, theta = 1e-10):
    random_actions = np.random.choice(
        tuple(P[0].keys()), len(P))
    pi = lambda s: {s:a for s, a in enumerate(
        random_actions)}[s]

    while True:
        old_pi = {s : pi(s) for s in range(len(P))}

        V = policy_evaluation(pi, P, gamma, theta)

        pi = policy_improvement(V, P, gamma)

        if old_pi == {s : pi(s) for s in range(len(P))}:
            break

    return V, pi



if __name__ == '__main__':
    pass