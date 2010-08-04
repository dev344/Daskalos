# ########################################################################################################################
# Date : 23rd July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################
"""
    This is the main script that needs to be run to start daskalos.
"""

import sys, os

pathname = os.path.dirname(sys.argv[0])     
full_path = os.path.abspath(pathname)
os.environ["DSK_HOME"] = full_path
ui_path = os.path.join(full_path, 'src/ui/')
if os.path.isfile(os.path.join(ui_path, "daskalosui.py")):
    sys.path.append(ui_path)
    ui_file = __import__('daskalosui')
    ui_file.daskalosUI.main()
else :
    print 'daskalosui.py file does not exist.Check if you are in the right folder'
os.environ.pop("DSK_HOME")
