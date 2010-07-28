# ########################################################################################################################
# Date : 23rd July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################
import time

class Dialogbox:

    def mainwindow_start_tut_BTN(self,daskalosUI):
        try:
            if daskalosUI.selected_filename:
                daskalosUI.window2.hide()
                daskalosUI.dialogbox.show_all()
                daskalosUI.dialogbox.set_keep_above(True)
        except Exception, e:
            pass
        #try :
        module = __import__(daskalosUI.selected_filename)
        time.sleep(1)
        try:
            module.tutorial.part.next()
        except Exception,e:
            reload(module)
            module.tutorial.part.next()
        #except Exception, e:
        #    print "Couldn't import ", daskalosUI.selected_filename
        #daskalosUI.run_tutorial()
        #daskalosUI.on_stop_BTN_pressed()
    
    def dialogbox_next_BTN_clicked(self,daskalosUI):
        try :
            module = __import__(daskalosUI.selected_filename)
            module.tutorial.part.next()
        except Exception, e:
            message = 'The tutorial has ended!\n Press return to go back.'
            daskalosUI.dialog_description_label.set_label(message)
            daskalosUI.stop_BTN.set_label('Return')
            daskalosUI.next_BTN.hide()
        
dialogboxUI = Dialogbox()
