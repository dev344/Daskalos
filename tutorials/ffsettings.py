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
   		Small explanation for the code : Functions like click, focus.frame, etc are all part of dogtail's procedural module
   										 which is imported in the observer module.
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-

def mainProgram():
	""" In this function things are hardcoded a bit.Also dogtail modules are imported inside.
	"""
	from observer import *                             #if i am using * then i should mention what all come under * later
	import dogtail.rawinput

	observer = Observer()                              


	observer.openWindow('Applications', 'Internet', 'Firefox Web Browser')
	if(not observer.isFocussed('Firefox')):                         #if i can somehow avaid such statements i can make this code more general i think
		raise NameError("Could not focus Firefox")       
     
	children_of_firefox = FocusApplication.node.children
	newWindowNum = len(children_of_firefox) - 1
	frameName = children_of_firefox[newWindowNum].name
	if(not observer.frameFocussed(frameName)): 
		raise NameError("Could not focus frame " + frameName)
	
	click('Edit', roleName='menu')
	click('Preferences', roleName='menu item')
	dogtail.rawinput.doTypingDelay()                #These delays have been included because  
	dogtail.rawinput.doTypingDelay()                #children_of_firefox is being found out 
	dogtail.rawinput.doTypingDelay()                #a bit earlier and hence there could be 
	dogtail.rawinput.doTypingDelay()                #a index out of range without this.
	children_of_firefox = FocusApplication.node.children
	prefWindowNum = len(children_of_firefox) - 1
	if(prefWindowNum <= newWindowNum ): 
		raise NameError("Preference window did not open")        
	prefWindow = children_of_firefox[prefWindowNum].name
	if(not(prefWindow == "Firefox Preferences")):                     #double-check.Can also be removed to make the code more general
		raise NameError("Preference Window did not open")
	if(not observer.frameFocussed(prefWindow)): 
		raise NameError("Could not focus frame " + prefWindow)
	
	click('Advanced')
	click('Network')
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
		raise NameError("Could not focus frame " + cnctn_sttngs_win)
		
def main():
	import subprocess
	mainProgram()
	
if __name__=='__main__' :
    main()
