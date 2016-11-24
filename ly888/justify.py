def justify(positions):
    # justify if the inputs is a list of integers
    d=len(positions);
    # if all are integers, set flag=0
    flag=0;
    for i in range(d):
        # if the one input is not integer, quit and return flag=1
        if positions[i].isdigit()==False:
            flag=1;
            break;
    return flag
