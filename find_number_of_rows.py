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
    rows=data.split('\n')
    print(rows)
    
    for x in rows:
        idx+=1

    return idx

    

# Read the csv file
