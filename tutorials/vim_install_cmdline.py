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
   		What the next few lines do : This code opens gnome-terminal via gnome-panel and installs vim.This can be generalised
   									 to install any software or to even type any command in the terminal.
   		
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from tutorial import *



class CommandLineInstall(Tutorial):

	header = 'How to install via commandline'
	
	Description = 'This is the CommandLine Install Tutorial Description'
	
	def mainProgram(self):
		""" In this function things are hardcoded a bit.Also dogtail modules are imported inside.
		"""
		#####types#####
		# observer : object of class Observer
		# children_of_gnometerm : list of objects of class Accessibility.Accessible    *i think
		# index_of_frame : integer
		# frameName : string
		
		from observer import Observer
		from dogtail.procedural import FocusApplication, click, keyCombo, type
		import dogtail.rawinput
		
		observer = Observer()  
	
	
		observer.openWindowFromMenu('Applications', 'Accessories', 'Terminal')
		if(not observer.isFocussed('gnome-terminal')): 
			raise Error("Could not focus gnome-termnal")
		
		children_of_gnometerm = FocusApplication.node.children
		index_of_frame = len(children_of_gnometerm)-1                           #index of last created frame
		frameName = children_of_gnometerm[index_of_frame].name
		if(not observer.frameFocussed(frameName)): 
			raise Error("Could not focus frame " + frameName)
		
		type("sudo apt-get install vim ")
		keyCombo("Return")                                                      #i am still debating whether to include this line or not
		
	def run(self):
		self.mainProgram()
		
tutorial = CommandLineInstall()
		
def main():
	import subprocess
	tutorial.mainProgram()
	
if __name__=='__main__' :
    main()
