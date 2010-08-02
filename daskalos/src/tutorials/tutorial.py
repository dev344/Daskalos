 # ########################################################################################################################
# Date : 23rd July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################   

"""
    This file describes how the basic structure of the tutorials should be.
"""    

class Error(Exception):
	def __init__(self, errorMessage = 'Daskalos Error occured.'):
		print errorMessage
 
class Tutorial:
    """
    	This should be the general structure of the tutorial.
    	mainProgram() should be the function inside which dogtail modules are imported
    """
    
    
    header = ''
    Author = 'Devesh Yamparala <dev344@gmail.com>'
    Description = ''
    duration = ''
    
    def __init__(self):
        pass
            
	def mainProgram(self):
		pass
		
    def run(self):
        pass
               
    def cleanup(self):
        pass

