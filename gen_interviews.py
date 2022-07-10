"""Generates the interview preparation data."""

import numpy as np
from math import exp

def main():
    print("Candidate,HRS,RESULT")
    for k in range(550):
        HRS = np.random.randint(-10, 10+1)
        if np.random.rand() <= 1/(1+exp(-0.345*HRS)):
            # successful candidate
            RES = 1
        else:
            # unsuccessful candidate
            RES = 0

        print(f"{k},{HRS},{RES}")

if __name__ == '__main__':
    main()
