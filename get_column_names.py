#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    coloumn=data.split('\n')
    coloumn_list=coloumn[0].split(',')
    return coloumn_list
    
    
# Read the csv file
f=open('data.csv').read()
print(get_column_names(f))