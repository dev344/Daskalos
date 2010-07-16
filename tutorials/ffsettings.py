# ########################################################################################################################
# Date : 15th July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# ########################################################################################################################

    """
    	What the next few lines do : This code here uses dogtail to open the network settings in firefox.
    	Small explanation for the code : 
    """
#!/usr/bin/python
# -*- coding: utf-8 -*-
from dogtail.procedural import *
import dogtail.rawinput

trylimit=0

focus.application('gnome-panel')
#focus.frame('Top Expanded Edge Panel')             #This line has to be removed completely later
click('Applications', roleName='menu')
click('Internet', roleName='menu')
click('Firefox Web Browser', roleName='menu item')
while((not focus.application('Firefox'))and(trylimit<30)):
    trylimit += trylimit

children_of_firefox = FocusApplication.node._getChildren()
framename = children_of_firefox[0]._get_name()
focus.frame(framename)
click('Edit', roleName='menu')
click('Preferences', roleName='menu item')
dogtail.rawinput.doTypingDelay()                #These delays have been included because  
dogtail.rawinput.doTypingDelay()                #children_of_firefox is being found out 
dogtail.rawinput.doTypingDelay()                #a bit earlier and hence there could be 
dogtail.rawinput.doTypingDelay()                #a index out of range without this.
children_of_firefox = FocusApplication.node._getChildren()
preference_window = children_of_firefox[1]._get_name()
focus.frame(preference_window)
click('Advanced')
click('Network')
scroll_pane = children_of_firefox[1]._getChildren()
panel = scroll_pane[7]._getChildren()      #scroll_pane[7] is Advanced options
scroll_pane2 = panel[0]._getChildren()    
panel2 = scroll_pane2[2]._getChildren()
next_child = panel2[0]._getChildren()       #panel2 is Connection option in Network option in Advanced options
settings = next_child[2]
x,y = settings.position
dogtail.rawinput.click(x, y, 1)
children_of_firefox = FocusApplication.node._getChildren()
cnctn_sttngs_win = children_of_firefox[2]._get_name()
focus.frame(cnctn_sttngs_win)
