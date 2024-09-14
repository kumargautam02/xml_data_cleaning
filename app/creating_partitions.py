import csv
import os
import json
import sys
import copy
from methods.mapping_file import *


def write_partitioned_data(partitioned_data, output_path):
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
        raise Exception("Error has occured at create_csv_file", e)

def partitioning_data_based_on_column(file_path, partitioned_column, output_path):

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # print(reader.json())
        creating_partition = {}
        for row in reader:
            sys.stdout.write(str(row))
            # print("outside",row["measInfoId"])
            if row[partitioned_column] not in creating_partition.keys():
                # print("onlu one",creating_partition)
                creating_partition[row[partitioned_column]] = [copy.deepcopy(row)]
                # print("onlu one1",creating_partition)
                # print("this blovk will run only 1 time",row["measInfoId"])
                # print(row["measInfoId"])
            else:
                # print("we are here ", row)
                # print("23 one",creating_partition)
                # print(creating_partition[row["measInfoId"]])
                # print("id", str(row[partitioned_column]))
                # print("inside", (creating_partition[str(row[partitioned_column])]))
                (creating_partition[str(row[partitioned_column])]).append(copy.deepcopy(row))
            # break
            # print(creating_partition[row["measInfoId"]])
        # print(creating_partition)
    write_partitioned_data(creating_partition, output_path)