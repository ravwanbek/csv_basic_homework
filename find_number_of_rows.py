from itertools import count


def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    
    idx=0
    coloumn=data.split('\n')
    coloumn_len=coloumn[idx].split(',')
    for x in coloumn:
        idx+=1

    return idx

    

# Read the csv file
