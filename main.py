import sys
import os
from app.creating_partitions import *
from app.flattening_xml_script import flatten_xml_file


if __name__ == "__main__":
    path = "C:/Users/Admin/Desktop/python_projects/xml-file-project/A20200314.1200+0200-1230+0200_MBTS_06330_VO_BBU0_IERAPETRA_NORTH.xml"
    
    
    # flatten_xml_file(path)
    flatten_xml_file(path)
    sys.stdout.write("SUCCESSFULLY COMPLETED SCRIPT flatten_xml_file")

    partitioning_data_based_on_column("output.csv", "measInfoId", str(os.getcwd()+'/'))
    sys.stdout.write("SUCCESSFULLY COMPLETED SCRIPT partitioning_data_based_on_column")