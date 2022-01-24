def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    
    new_list=[]
    coloumn=data.split('\n')
    
    
    for idx in range(len(coloumn)):
        coloumn2=coloumn[idx].split(',')
        a=coloumn2[0]
        new_list.append(a)

    return new_list
    
# Read the csv file
