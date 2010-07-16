#!/usr/bin/python
from dogtail.procedural import *

focus.application('gnome-panel')
focus.frame('Top Expanded Edge Panel')
click('System', roleName='menu')
click('Administration', roleName='menu')
click('Synaptic Package Manager', roleName='menu item')
#focus.application('Synaptic Package Manager')
focus.frame('Synaptic Package Manager')

rawinput.typeText('abcd')
