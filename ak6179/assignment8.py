# Author: Abhishek Kadian <ak6179@nyu.edu>

import simulation
import argparse
import sys
import logging


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-enter_positions", default=0, type=int)
        args = parser.parse_args()
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        if args.enter_positions == 1:
            try:
                p_input = input("Comma separated positions: ")
                positions = [int(x) for x in p_input.strip().split(",")]
                num_trials = int(input("Number of trials: "))
            except KeyboardInterrupt:
                print("KeyboardInterrupt, exiting.")
                sys.exit()
            except Exception as e:
                print(e)
                print("ValueError: positions should be a comma(',') separated list of integers.")
                print("ValueError: number of trials should be an integer.")
                sys.exit()
        else:
            positions = [1, 10, 100, 1000]
            num_trials = 10000
        output_files = ["histogram_" + '{:04d}'.format(p) + "_pos.pdf" for p in positions]
        sim = simulation.Simulation(positions, num_trials)
        logging.info("Running simulation.")
        sim.simulate()
        logging.info("Simulation over.")
        results_path = "results.txt"
        sim.write_summary(results_path)
        logging.info("Results summary written to: " + results_path)
        sim.plot_trials_histogram(output_files)
        logging.info("Histograms written to files: " + str(output_files))
    except KeyboardInterrupt:
        print("KeyboardInterrupt, exiting.")
        sys.exit()


if __name__ == "__main__":
    main()
