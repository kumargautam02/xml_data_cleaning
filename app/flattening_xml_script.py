import re
import os
import copy
import xml.etree.ElementTree as ET
from methods.mapping_file import *
from methods.common_functions import *
from app.creating_partitions import *



def flatten_xml_file(path):
    """
    This function is used to flatten the xml file.
    """
    try:
        rows = []
        temp_dict = {}
        
        input_file_name = extract_input_file_name(path)
        print(input_file_name)
        tree = ET.parse(path)
        root = tree.getroot()
        file_namespace = root.tag.split("}")[0] + "}"

        temp_dict["input_file_name"] = input_file_name
        for root_child in root:
            if str(root_child.tag).__contains__('fileHeader'):
                temp_dict['fileFormatVersion'] = root_child.attrib['fileFormatVersion']
                temp_dict['vendorName'] = root_child.attrib['vendorName']
                temp_dict['elementType'] = root_child.find(f"{file_namespace}fileSender").attrib['elementType']
                temp_dict['beginTime'] = root_child.find(f"{file_namespace}measCollec").attrib['beginTime']
            if str(root_child.tag).__contains__('measData'):
                for measInfo_child in root_child.findall(f"{file_namespace}measInfo"):
                    temp_dict['userLabel'] = root_child.find(f"{file_namespace}managedElement").attrib['userLabel']
                    temp_dict['measInfoId'] = measInfo_child.attrib['measInfoId']
                    temp_dict['duration'] = measInfo_child.find(f"{file_namespace}granPeriod").attrib['duration']
                    temp_dict['endTime'] = measInfo_child.find(f"{file_namespace}granPeriod").attrib['endTime']
                    temp_dict['measTypes'] = measInfo_child.find(f"{file_namespace}measTypes").text.replace(" ", ",")
                    for measValue_child in measInfo_child.findall(f"{file_namespace}measValue"):
                        temp_dict['measResults_row_values'] = measValue_child.find(f"{file_namespace}measResults").text.replace(" ", ",")
                        #using deepcopy to change the reference address.
                        rows.append(copy.deepcopy(temp_dict))
        create_csv_file(rows)
    except Exception as e:
        raise Exception("Error has occured at create_csv_file", e)