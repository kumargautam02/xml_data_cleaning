import csv
import os
import json
import sys
import copy
from methods.mapping_file import *


def write_partitioned_data(partitioned_data, output_path):
    """
    This function is used to create partitions
    """
    try:
        # working_dir = str(os.getcwd()+'/').replace("\\", "/")
        # print(f"Your Working Directory is: {working_dir}")
        print(output_path)
        if "partitioned_data" not in os.listdir(output_path):
            os.makedirs(f'{output_path}partitioned_data')

        
        for file_names in partitioned_data.keys():
            with open(f'{output_path}/partitioned_data/{file_names}.csv','w', newline='') as csvfile:
                print(len(partitioned_data[file_names]))
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(partitioned_data[file_names])

    except Exception as e:
        raise Exception("Error has occured at write_partitioned_data", e)

def partitioning_data_based_on_column(file_path, partitioned_column, output_path):
    """
    This function is used to partition the data
    """

    try:

        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # print(reader.json())
            creating_partition = {}
            for row in reader:
                sys.stdout.write(str(row))

                if row[partitioned_column] not in creating_partition.keys():

                    creating_partition[row[partitioned_column]] = [row]

                else:
                    (creating_partition[str(row[partitioned_column])]).append(row)

        write_partitioned_data(creating_partition, output_path)
    except Exception as e:
        raise Exception("Error has occured at partitioning_data_based_on_column", e)