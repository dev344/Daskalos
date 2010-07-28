# ########################################################################################################################
# Date : 23rd July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################

import sys, os

pathname = os.path.dirname(sys.argv[0])     
full_path = os.path.abspath(pathname)
os.environ["DSK_HOME"] = full_path
ui_path = os.path.join(full_path, 'src/ui/')
if os.path.isfile(os.path.join(ui_path, "gladepreview.py")):
    sys.path.append(ui_path)
    ui_file = __import__('gladepreview')
    ui_file.daskalosUI.main()
else :
    print 'gladepreview.py file does not exist.Check if you are in the right folder'
os.environ.pop("DSK_HOME")
