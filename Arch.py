# Arch.py
# Import the argparse library
import argparse

import os
import sys
import json

import Composer

from diagrams import Cluster, Diagram

# Create the parser
my_parser = argparse.ArgumentParser(prog='Architecture Automation',
                                    usage='%(prog)s [options] ConfigFile',
                                    description='Automate the process of creating HLD',
                                    epilog='Enjoy the program! :)')

# Add the arguments
my_parser.add_argument('ConfigFile',
                       metavar='Configuration file path',
                       type=str,
                       help='configuration file path')

# Execute the parse_args() method
#args = my_parser.parse_args()

#input_path = args.ConfigFile
input_path = "template.json"

if not os.path.isfile(input_path):
    print ('Incorrect input file')
    sys.exit()

with open(input_path) as jsonFile:
  data = json.load(jsonFile)

# Draw
flatlist = {}
with Diagram(data["diagram_name"], show=False) as diagram:
  Composer.BuildModel(data["components"], flatlist)
  Composer.LinkModel(data["connections"], flatlist)

#document
#Composer.CreateWordDocument(data)
    
#sys.exit()