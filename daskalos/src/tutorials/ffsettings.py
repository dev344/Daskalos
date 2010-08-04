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
   		What the next few lines do : This code here uses dogtail to open the network settings in firefox.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from tutorial import *

class FirefoxTutorial(Tutorial):
	
	header = 'How to change Network Settings in Firefox'
	
	Description = ''
	
	lines = ['To change your network settings in Firefox Web Browser you need to',
		  "\n- Click on 'Applications' menu ,from gnome-panel, on the top-left corner",
		  "\n- Click on 'Internet' menu item from the menu and select 'Firefox Web Browser'",
		  "\n- After the browser opens click on 'Edit' menu ,on top-left, and choose\n' Preferences' menu item",
		  "\n- After the new window opens click on the 'Advanced' tab,which is on \n top-right",
		  "\n- Select the 'Network' tab and click on the 'Settings' button and make\n necessary settings" ]
	
	DialogBox_label = ''
	
	for line in lines :
		Description = Description + line
	
	tags = 'Firefox browser web network settings internet'
	
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
	
	
		observer.openWindowFromMenu(['Applications', 'Internet', 'Firefox Web Browser'])
		if(not observer.isFocussed('Firefox')):                         #if i can somehow avoid such statements i can make this code more general i think
			raise Error("Could not focus Firefox")       
    
		children_of_firefox = FocusApplication.node.children
		newWindowNum = len(children_of_firefox) - 1
		frameName = children_of_firefox[newWindowNum].name
		if(not observer.frameFocussed(frameName)): 
			raise Error("Could not focus frame " + frameName)
		
		click('Edit', roleName='menu')
		click('Preferences', roleName='menu item')
		time.sleep(2)
		children_of_firefox = FocusApplication.node.children
		prefWindowNum = len(children_of_firefox) - 1
		if(prefWindowNum <= newWindowNum ): 
			raise Error("Preference window did not open.Please make sure nothing interferes with the focussing of the created window.")        
		prefWindow = children_of_firefox[prefWindowNum].name
		if(not(prefWindow == "Firefox Preferences")):                     #double-check.Can also be removed to make the code more general
			raise Error("Preference Window did not open")
		if(not observer.frameFocussed(prefWindow)): 
			raise Error("Could not focus frame " + prefWindow)
		
		click('Advanced')
		time.sleep(1)
		click('Network')
		time.sleep(1)
		scroll_pane = children_of_firefox[prefWindowNum].children
		panel = scroll_pane[7].children       #scroll_pane[7] is Advanced options
		scroll_pane2 = panel[0].children    
		panel2 = scroll_pane2[2].children
		next_child = panel2[0].children       #panel2 is Connection option in Network option in Advanced options
		settings = next_child[2]
		x,y = settings.position
		dogtail.rawinput.click(x, y, 1)
		children_of_firefox = FocusApplication.node.children
		cntnsWindowNum = len(children_of_firefox) - 1
		cnctn_sttngs_win = children_of_firefox[cntnsWindowNum].name
		if(not observer.frameFocussed(cnctn_sttngs_win)): 
			raise Error("Could not focus frame " + cnctn_sttngs_win)
		
	def run(self):
		self.DialogBox_label = 'Now you can set your network settings here by\n filling up the appropriate fields'
		self.mainProgram()
		yield
			
tutorial = FirefoxTutorial()	
	
def main():
	import subprocess
	tutorial.mainProgram()
	
if __name__=='__main__' :
    main()
