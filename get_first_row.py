def get_first_row(data):   
    """
    Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
    """
    row=data.split('\n')
    row_1=row[1].split(',')
    return row_1
    
# Read the csv file
