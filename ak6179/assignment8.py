# Author: Abhishek Kadian <ak6179@nyu.edu>

import simulation


def main():
    positions = [1, 10, 100, 1000]
    trials = 100
    sim = simulation.Simulation(positions, trials)


if __name__ == "__main__":
    main()
