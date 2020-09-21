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

#Ask User for search date
user_date = input ("Enter data to search for Sara: ")
#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionary objects
date_dict = {}
coord_dict = {}

# Iterate through all lines in the lineList
for lineString in line_list:
    if lineString[0] in ("#","u"): continue

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split()
    
    # Assign variables to specfic items in the list
    record_id = lineData[0]             # ARGOS tracking record ID
    obs_date = lineData[2]   # Observation date
    ob_lc = lineData[4]                 # Observation Location Class
    obs_lat = lineData[6]               # Observation Latitude
    obs_lon = lineData[7]               # Observation Longitude
    
    # Print information to the use
    if ob_lc in ("1","2","3"):
     #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")
     date_dict[record_id] = obs_date
     coord_dict[record_id] = (obs_lat,obs_lon)
  
 #Creat an empty list to holde matching keys
matching_keys = []
   
 #Loop through items in the date_dict and collect keys for matching ones
for date_item in date_dict.items():
    #Get the date of the item
    the_key, the_date = date_item
    #See if the date matches the user date
    if the_date == user_date:
        #if s, add the key to the list
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {user_date}")