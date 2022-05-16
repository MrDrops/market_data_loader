import numpy as np
import pandas as pd
import os
import re

# function to load all pair data files
def load_pair_data(pair_data_path='C:\\Users\\Drops\\Documents\\Trading_Files\\chart_data_files'):
    """
    loads pairData in pair_data_path
    returns dictionary of pair data in files
    """
    # Makes a list of the pair names
    pair_name_list = []
    for filename in os.listdir(pair_data_path):
        unique_name = filename[0:6]
        if unique_name not in pair_name_list:
            pair_name_list.append(unique_name)
    # Makes a dictionary key=pairname values=list of dataframes with the 4 timeframes
    # takes all files in path and puts the in the dictionary
    pair_data_dict = {}
    for unique_name in pair_name_list:
        pair_data_dict[unique_name] = []
        pair_re = re.compile('^{}.*'.format(unique_name, re.I))
        for filename in os.listdir(pair_data_path):        
            if pair_re.match(unique_name):
                os.chdir(pair_data_path)
                load_csv = pd.read_csv(filename,encoding='utf-16',
                    names=['date', 'open', 'high', 'low', 'close', 'volume', 'tickVol'],
                    index_col='date',header=1, parse_dates=True, infer_datetime_format=True)
                pair_data_dict[unique_name].append((filename, load_csv))
    print('done')
    return pair_data_dict

    # def pair_data_obj_maker(load_pair_data_output):
    #     """
    #     creates pair_data_objects
    #     input: dictionary output of load_pair_data
    #     return: 
    #     """
    #     for pair_data in load_pair_data_output:
    # #     # creates the pair_data_object
    # #     pair_data_object = None
    #     return pair_data_object