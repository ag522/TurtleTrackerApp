#---------------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Read in an ARGOS tracking data file and allows
# the user to view the location of the turtle for a specified 
# date entered via user input. 
#
# Author: Andrea Gonzalez (ag522@duke.edu)
# Date: Fall 2020
#---------------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()


# Copy and paste a line of data as the lineString variable value
lineString = line_list[100]
# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()
# Assign variables to specfic items in the list
record_id = lineData[0]             # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[4]                 # Observation Location Class
obs_lat = lineData[6]               # Observation Latitude
obs_lon = lineData[7]               # Observation Longitude
# Print information to the use
print("Record {} indicates Sara was seen at {}N and {}W on {}".format(record_id,obs_lat,obs_lon,obs_date))
