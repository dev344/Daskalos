# ########################################################################################################################
# Date : 15th July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################

"""
   		What the next few lines do : This code here is intended to open software sources and click at places to take you to 
   									 the place from where you can choose your repository.
   		Small explanation for the code : openWindowFromMenu function opens window using dogtail.After that xnee moves the mouse to 
   										 click at places. 
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
from tutorial import *
import subprocess



class SoftwareSources(Tutorial):

	header = 'How to change default repository'        #May need to state it better
	
	Description = 'This is the Software Sources Tutorial Description'
	def mainProgram(self):
		""" In this function things are hardcoded a bit.Also dogtail modules are imported inside.
		"""
	
		from observer import Observer
		
		observer = Observer()                              
		
		observer.openWindowFromMenu('System', 'Administration', 'Software Sources')
		time.sleep(4)
		
	def run(self):
		self.mainProgram()
		args = 'cnee --replay --no-synchronise --file ' + sys.argv[1]
		p = subprocess.Popen(args,shell= True)
		
tutorial = SoftwareSources()

def main():
	tutorial.mainProgram()
	args = 'cnee --replay --no-synchronise --file ' + sys.argv[1]
	p = subprocess.Popen(args,shell= True)
	    
if __name__=='__main__' :
    main()
