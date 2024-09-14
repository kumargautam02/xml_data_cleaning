import re
import csv
import traceback
from methods.mapping_file import *



def extract_input_file_name(path):
    """
    This funciton is used to extract input file name.
    """
    try:
        return path.split("/")[-1]
    except Exception as e:
        raise Exception("Error has occured ==> extract_input_file_name", e)
    

def create_csv_file(rows):
    """
    This function will create csv file and will write data into the csv file
    """
    try:
        with open('output.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except Exception as e:
        raise Exception("Error has occured at create_csv_file", e)