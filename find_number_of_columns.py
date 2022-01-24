def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list=[]
    coloumn=data.split('\n')
    coloumn_len=coloumn[0].split(',')




    return len(coloumn_len)

# Read the csv file
