from invest import invest
from justify import justify


def main():
    # the program is written by Lei Yang (ly888)
    # the main function to calculate and plot daily return. 
    # if the user input is not valid, the program will let the user to input again until valid or enter quit
    positions = input("Enter a list of the number of shares to buy in parallel: e.g. 1,10,100,1000 or stop this process by entering quit \n")
    positions_split = positions.split(",");
    # justify if the input value is valid
    flag=justify(positions_split);
    # if the user input quit, the program will stop. if the user input invalid value, the program will ask the user to input again
    while(positions != 'quit' and flag==1):
        positions=input("The last input is not valid. Please enter a list of the number of shares to buy in parallel: e.g. 1,10,100,1000 or stop this process by entering quit \n")
        if(positions =='quit'):
            break;
        positions_split = positions.split(",");
        # justify if the input value is valid
        flag=justify(positions_split);
    if(positions != 'quit'):  
        flag=0;
        num_trials = input("How many times to randomly repeat the test? Or stop this process by entering quit \n");
        # justify if the input value is valid
        if num_trials.isdigit()==False:
            flag=1;
        # if the user input quit, the program will stop. if the user input invalid value, the program will ask the user to input again
        while(num_trials != 'quit' and flag==1):
            flag=0;
            num_trials = input("The last input is not valid. How many times to randomly repeat the test? Or stop this process by entering quit \n");
            # justify if the input value is valid
            if num_trials.isdigit()==False:
                flag=1;
            if(num_trials == 'quit'):
                break;
    # if all the input are valid, the program will calculate the results and plot
    if(positions!='quit' and num_trials !='quit'):
        positions_list = [int(position) for position in positions_split];
        outcome = invest(positions_list, int(num_trials));
        outcome.invest_sub();

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interruption")