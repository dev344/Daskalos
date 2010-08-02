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
   		What the next few lines do : This code here is intended to use dogtail to open synaptic package manager and type vim.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from tutorial import Tutorial



class SynapticTutorial(Tutorial):
	
	header = 'How to install using Synaptic Package Manager'
	
	line = ['To install something using syanptic you need to',
			"\n- Click on 'System' menu ,from gnome-panel, on the top-left",
			"\n- Click on 'Administration' menu item from the menu and select\n 'Synaptic Package Manager'",
			"\n- You may need to type your password if you haven't in the near past",
			"\n- After the window opens type the name of the thing you want to\n install in the search bar(top middle)",
			"\n- Search for it in the list below.Select it by left clicking beside\n the name",
			"\n- Select the option'Mark for installation' and don't forget to\n 'Apply'(beside search bar)  ",]
	
	Description = line[0] + line[1] + line[2] + line[3] + line[4] + line[5] + line[6]
	
	DialogBox_label = ''
	
	tags = 'Installation Synaptic Package Manager Software'
	
	def __init__(self):
			self.part = self.run()
			
	def mainProgram(self):
		""" In this function things are hardcoded a bit.Also dogtail modules are imported inside.
		"""
		
		from observer import Observer                             
		import dogtail.rawinput
		
		observer = Observer()                              
		
		
		observer.openWindowFromMenu('System', 'Administration', 'Synaptic Package Manager')
		#frameName = 'Synaptic Package Manager'
		#if(not observer.frameFocussed(frameName,1)): 
		#	raise Error("Could not focus frame " + frameName)
		"""I am debating which to include.The above three lines or the next few lines.
		The above two lines will definitely raise an error and end while with the below few lines
		i can even type some name in many cases"""
		time.sleep(4)
		dogtail.rawinput.typeText('vim')
		
	def run(self):
		self.DialogBox_label = 'You can now search your package in the quick\n search bar and then select the required package\n by clicking at the selection button beside the\n name and selecting "Mark for Installation".\n Do not forget to apply this by clicking apply'
		self.mainProgram()
		yield
		
tutorial = SynapticTutorial()

def main():
	import subprocess
	tutorial.mainProgram()
	
if __name__=='__main__' :
    main()
