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

import sys,os
import time
from tutorial import *
import subprocess



class SoftwareSources(Tutorial):

	header = 'How to change default repository'        #May need to state it better
	
	line = ['To change your default repository you need to ',
			"\n- Click on 'System' menu ,from gnome-panel, on the top-left",
			"\n- Click on 'Administration' menu item from the menu and select\n 'Software Sources'",
			"\n- You may need to type your password if you haven't in the near past",
			"\n- After the new window opens click on the 'Ubuntu Software' tab,\n which is on top-left",
			"\n- In the 'Download from ' options select 'Other..' and choose one repo" ]
	
	DialogBox_label = ''
	
	Description = line[0] + line[1] + line[2] + line[3] + line[4] + line[5]
	
	tags = 'Software Sources Install repository '
	
	def __init__(self):
			self.part = self.run()
	
	def mainProgram(self):
		""" In this function things are hardcoded a bit.Also dogtail modules are imported inside.
		"""
	
		from observer import Observer
		
		observer = Observer()                              
		
		observer.openWindowFromMenu('System', 'Administration', 'Software Sources')
		time.sleep(4)
		
	def run(self):
		self.DialogBox_label = 'Now first choose your country and then\n choose a server from the list.Then click\n on "Choose Server" '
		self.mainProgram()
		file_path = os.path.join(os.path.expandvars("$DSK_HOME"), 'src/tutorials/sftwrsrcemouse.xnl')
		args = 'cnee --replay --no-synchronise --file ' + file_path
		p = subprocess.Popen(args,shell= True)
		yield
		
tutorial = SoftwareSources()

def main():
	tutorial.mainProgram()
	args = 'cnee --replay --no-synchronise --file ' + sys.argv[1]
	p = subprocess.Popen(args,shell= True)
	    
if __name__=='__main__' :
    main()
