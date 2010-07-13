#!/usr/bin/python
from dogtail.procedural import *

print 'blah'
focus.application('gnome-panel')
focus.frame('Top Expanded Edge Panel')
click('Applications', roleName='menu')
click('Accessories', roleName='menu')
click('Terminal', roleName='menu item')
focus.application('gnome-terminal')
children_of_gnometerm = FocusApplication.node._getChildren()
index_of_frame = len(children_of_gnometerm)-1         #index of last created frame
framename = children_of_gnometerm[index_of_frame]._get_name()
focus.frame(framename)
type("sudo apt-get install vim ")
keyCombo("Return")
