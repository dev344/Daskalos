# ########################################################################################################################
# Date : 23rd July 2010
# Written by : Devesh Yamparala
# Mentored by : Arun Chaganty
# For Application : Daskalos
# Applications used here : Dogtail-0.7.0
# Other info : This was written for the application Daskalos to be included in the distro 'Shaastra Distro'
# Contact : shaastra-distro-2010@googlegroups.com
# ########################################################################################################################
"""
	This is the code for the UI dialog box which appears while running tutorials. 
"""
import time

class Dialogbox:

    def mainwindow_start_tut_BTN(self,daskalosUI):
        try:
            if daskalosUI.selected_filename:
                daskalosUI.window2.hide()
                daskalosUI.dialogbox.show_all()
                daskalosUI.dialogbox.set_keep_above(True)
                daskalosUI.replay_BTN.hide()
        except Exception, e:
            pass
        try :
            module = __import__(daskalosUI.selected_filename)
            time.sleep(1)
            module.tutorial.part.next()
            try :
                daskalosUI.dialog_description_label.set_label( module.tutorial.DialogBox_label )
            except Exception :
                pass
        except Exception,e:
            # Here,this exception is raised mainly when the tutorial has been already run and 
            # replay button has been pressed.
            reload(module)
            module.tutorial.part.next()
            try :
                daskalosUI.dialog_description_label.set_label( module.tutorial.DialogBox_label )
            except Exception :
                pass
            

    
    def dialogbox_next_BTN_clicked(self, daskalosUI):
        try :
            module = __import__(daskalosUI.selected_filename)
            module.tutorial.part.next()
            try :
                daskalosUI.dialog_description_label.set_label( module.tutorial.DialogBox_label )
            except Exception :
                pass
        except Exception, e:
            message = 'The tutorial has ended!\n Press return to go back\n or replay to show it again\n\n Do not forget to close any\n administrative windows if open.'
            daskalosUI.dialog_description_label.set_label(message)
            daskalosUI.stop_BTN.set_label('Return')
            daskalosUI.next_BTN.hide()
            daskalosUI.replay_BTN.show()
        
    def dialogbox_replay_BTN_clicked(self, daskalosUI):
        daskalosUI.stop_BTN.set_label('Stop')
        daskalosUI.dialog_description_label.set_label('')
        self.mainwindow_start_tut_BTN(daskalosUI)
        
dialogboxUI = Dialogbox()
