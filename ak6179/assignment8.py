"""
Author: Abhishek Kadian <ak6179@nyu.edu>
Driver program for running simulation.
By default the program runs simulation on position: [1, 10, 100, 1000] for num_trials: 10000.
The user can also input a list of positions and num_trials at command line
by running the program using the command: 'python assignment8.py -enter_positions 1'.
The positions entered at command line should be comma separated, eg: "1, 10, 100, 1000".
The positions and num_trials entered should be integer.
Info messages are also logged describing the state of program.
Please use python3 for running the program.
The mean and std-deviation of simulation is written to 'results.txt'.
Histograms for different positions are also saved to .pdf files.
For running the unit test use the command 'python -m unittest discover' in the netid (ak6179) directory.
The command will automatically discover unit tests and will run them.
"""
import simulation
import argparse
import sys
import logging


def main():
    try:
        parser = argparse.ArgumentParser()
        # Adding option to allow user to enter positions, num_trials at command line.
        parser.add_argument("-enter_positions", default=0, type=int)
        args = parser.parse_args()
        # Setting up logging to give info about different states of the program.
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
        # Creating paths for histogram files according to names specified in the assignment.
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
