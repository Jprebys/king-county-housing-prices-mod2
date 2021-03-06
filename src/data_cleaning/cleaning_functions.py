def lower_cols(lst_of_dfs):
    """
    This function takes a list of pandas dataframes and makes all the column headers lower case
    Returns the updated dfs
    """
    for df in lst_of_dfs:
        colnames = list(map(lambda x: x.lower(), df.columns))
        df.columns = colnames
        
    return lst_of_dfs




def padded(row, pad_to):
    """
    This function takes an index item and pads it with 0's at the beginning
    to make it's total length equal to the pad_to value. 
    
    arguments:
    row (str):  item to add 0's infront of
    pad_to (int):  total length of padded item
    """
    num_zeros = pad_to - len(row)
    return num_zeros * '0' + row

def major_pad(row):
    """
    This function takes an index item and pads it with 0's at the beginning
    to make it's total length equal to the pad_to value. 
    
    arguments:
    row (str):  item to add 0's infront of
    pad_to (int):  total length of padded item
    """
    num_zeros = 6 - len(row)
    return num_zeros * '0' + row

def minor_pad(row):
    """
    This function takes an index item and pads it with 0's at the beginning
    to make it's total length equal to the pad_to value. 
    
    arguments:
    row (str):  item to add 0's infront of
    pad_to (int):  total length of padded item
    """
    num_zeros = 4 - len(row)
    return num_zeros * '0' + row


def maj_min_col(table):
    """
    Takes a table with a Minor and Major column, pads the Minor and Major columns with 0's at the beginning and then 
    concatenates Major and Minor together in a new column with the 10-digit number and sets it as the table index. 
    It also drops the old major/minor columns from the table
    """
    
    # change minor/minor to str
    table['major'] = table['major'].astype(str)
    table['minor'] = table['minor'].astype(str)
    
    # add padding to major/minor
    table['major'] = table['major'].apply(major_pad)
    table['minor'] = table['minor'].apply(minor_pad)
    
    # add maj_min column
    table['major_minor'] = table['major'] + table['minor']
    
    # drop old major/minor columns
    table.drop(labels = ['major', 'minor'], axis = 1, inplace = True)
    
    # make 'major_minor' column the first column
    col_name = 'major_minor'
    last_col = table.pop(col_name)
    table.insert(1, col_name, last_col)
    
    return table

def lower_cols(table):
    """
    A function that takes a table and makes all the columns lower case
    table (pd dataframe)
    """
    table.rename(columns = str.lower, inplace=True)
    
    return table

