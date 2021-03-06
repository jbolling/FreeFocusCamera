import csv
import os.path as path
import os
import numpy as np

#Returns a MxNx2 array of [yaw, pitch] pairs for every image pixel, loaded from 
#the data in template_dir
def load_angles(template_name):
	#Check that template directory exists
	template_dir = path.join(os.getcwd(),'Scan Templates',template_name)
	if(not path.isdir(template_dir)):
		raise Exception("Template directory not found: " + template_dir)
		
	#Check that files exist
	pitch_angles_file = path.join(template_dir,'pitch_angles.csv')
	yaw_angles_file = path.join(template_dir,'yaw_angles.csv')
	if(not path.isfile(pitch_angles_file) or not path.isfile(yaw_angles_file)):
		raise Exception("Corrupt template directory")
	
	#Create angle arrays
	with open(yaw_angles_file, 'r') as f:
		yaw_reader = csv.reader(f, delimiter=",")
		yaw_angles = np.rint(np.array(list(yaw_reader)).astype(float)).astype(int)
	with open(pitch_angles_file, 'r') as f:
		pitch_reader = csv.reader(f, delimiter=",")
		pitch_angles = np.rint(np.array(list(pitch_reader)).astype(float)).astype(int)
	
	return np.stack((yaw_angles,pitch_angles),axis=2)
	
