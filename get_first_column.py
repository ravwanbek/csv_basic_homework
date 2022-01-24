def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    coloumn=data.split('\n')
    coloumn_1=coloumn[1].split(',')
    return coloumn_1
    
# Read the csv file