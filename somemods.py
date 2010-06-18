################################################################################################
#This is a file with some functions which take input of either a file location or x,y coordinates and then uses xnee to perform the task.
#this is my attempt to run shell commands thru python.

#########################################
#this was an initail attempt to try somethings.....unnecessary or rather a dumb way of doing things
""" def input_from_file(file_location):
		file_location_pointer=open(file_location,'r')                                       #opening file pointer which points to the file
		for line in file_location_pointer.readlines():                  
			print 'hello'
			if '\n' in line:
				args = 'echo "' + line[:-1] + '" |cnee --replay --file stdin \n'      #if the line ends with \n remove it and include it in the string args 
			else:
				args = 'echo "' + line[:] + '" |cnee --replay --file stdin \n'
				
			p = subprocess.Popen(args,shell= True)                                          #to execute the command(or actually a pipe here) stored in 'args' in the shell
		
		file_location_pointer.close()      """
		
###################################		
#this is a function which takes as input a file location
def input_from_file(file_location):
	args = 'cnee --replay --file ' + file_location
	p = subprocess.Popen(args,shell= True)
	

###################################
def input_direct_mouse(x, y,time):
	xnee_instruction = 'fake-motion x=' + repr(x) + ' y=' + repr(y) + ' msec=' + repr(time)
	args = 'echo "' + xnee_instruction + '" | cnee --replay --file stdin '
	p = subprocess.Popen(args,shell= True)
	
####################################
