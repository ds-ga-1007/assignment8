# Author: Abhishek Kadian <ak6179@nyu.edu>

import simulation


def main():
    positions = [1, 10, 100, 1000]
    trials = 10000
    sim = simulation.Simulation(positions, trials)
    sim.simulate()
    sim.write_summary("results.txt")
    sim.plot_trials_histogram(filepath_prefix="histogram_")

if __name__ == "__main__":
    main()
