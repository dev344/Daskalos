# ########################################################################################################################
# Date : 3rd September 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################

"""
   		What the next few lines do : This code here uses dogtail to take you to Ubuntu Software Center.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from tutorial import *

class SoftwareCenter(Tutorial):
	
	header = 'How to install new softwares(for free!)or remove them'
	
	Description = ''
	
	lines = ['To install or remove softwares using ubuntu software center you need to',
		  "\n- Click on 'Applications' menu from gnome-panel, on the top-left corner",
		  "\n- Click on 'Ubuntu Software Center' menu item from the menu",
		  "\n- After the window opens you can either search in the search bar at the\n top-right corner or select a department and see the softwares in it.",
		  "\n- Then select the software you want and press install or remove button \n on the right most side of the name of the software." ]
	
	DialogBox_label = ''
	
	for line in lines :
		Description = Description + line
	
	tags = 'Install graphically easy new remove software center centre free applications available'
	
	def __init__(self):
			self.part = self.run()
	        
	def mainProgram(self):
		""" In this function things are hardcoded a bit.Also dogtail modules are imported inside.
		"""
		####types####
		# observer : object of class Observer
		# children_of_firefox : list of objects of class Accessibility.Accessible    
		# prefWindowNum,newWindowNum : integer
		# frameName = string
		
		from observer import Observer
		from dogtail.procedural import FocusApplication, click                             
		import dogtail.rawinput
	
		observer = Observer()                              
	
	
		observer.openWindowFromMenu(['Applications', 'Ubuntu Software Center'])
		if(not observer.isFocussed('software-center')):                         #if i can somehow avoid such statements i can make this code more general i think
			raise Error("Could not focus Ubuntu Software Center")       
    
		
		
	def run(self):
		self.DialogBox_label = 'Search in the search bar at the top-right\ncorner or select a department.\nThen select the software you want and press\n install or remove button on the right most.'
		self.mainProgram()
		yield
			
tutorial = SoftwareCenter()	
	
def main():
	import subprocess
	tutorial.mainProgram()
	
if __name__=='__main__' :
    main()
