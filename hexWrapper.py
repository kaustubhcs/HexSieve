import subprocess
import sys
import os
import configparser
from time import time

import functions

"""
    runHex is a function that wraps over the hex executable file to run the program
    with the specified startpoint->color and with a specific endpoint.
"""
def runHex (startpoint, startpointColor, endpoint):
    args = ("./hex", str(startpoint), str(startpointColor), str(endpoint))
    #print ("Running ", args)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    output = eval(output)
    return output

def hexSeek(head_dir,endpoint):

    print ("Reading Configuration File")
    
    settings = configparser.ConfigParser()
    settings._interpolation = configparser.ExtendedInterpolation()
    settings.read('config.ini')#

    # Config variables
    path_dec = eval(settings.get('DIRCONFIG', 'PATH_DECIMALS'))
    file_dec = eval(settings.get('DIRCONFIG', 'FILE_DECIMALS'))
    run_dec  = eval(settings.get('DIRCONFIG', 'RUN_DECIMALS'))
    goal_dec = eval(settings.get('DIRCONFIG', 'GOAL_DECIMALS'))
   
    # Check which is the latest directory/file created and look for the last checkpoint stored to start from there.
    
    end_str = str(endpoint).zfill(goal_dec)
    dir_str = end_str[:path_dec]
    dir_str = head_dir+'/'+dir_str[:1]+'/'+dir_str[1:3]+'/'+dir_str[3:path_dec]
    file_line = int(end_str[path_dec:(path_dec+file_dec)])
            
    if not os.path.exists(dir_str):
        return "ERROR File input required not found!"
        
    start_color = functions.fileLineColor(file_line,dir_str)
    
    if start_color == -1:
        print ("Mistake")
        return -1
    
    # If no errors, good to run the hex code
    if end_str == end_str[:(path_dec+file_dec)]+''.zfill(run_dec):
        return start_color
        
    return runHex(end_str[:(path_dec+file_dec)]+''.zfill(run_dec),start_color,endpoint)