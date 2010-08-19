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
            This is the UI for Daskalos.
"""

import gtk, gobject
import sys, os, subprocess, time

class DaskalosUI:

    tutorial_path = os.path.join(os.path.expandvars("$DSK_HOME"), 'src/tutorials/')
    images_path = os.path.join(os.path.expandvars("$DSK_HOME"), 'src/screenshots/')
    UIFile = os.path.join(os.path.expandvars("$DSK_HOME"), 'src/ui/daskalosMain.glade')
    
    def main(self):
        builder = gtk.Builder()
        builder.add_from_file(self.UIFile)
        signal_connections = { "on_start_tut_BTN_button_press_event" : self.start_tut_BTN_button_press_event, 
                                'on_searchbar_changed' : self.searchbar_changed, 
                                "button-release-event" : self.run_tutorial,
                                'on_treeview1_cursor_changed' : self.cursor_changed, 
                                'on_stop_BTN_pressed' : self.on_stop_BTN_pressed,
                                'gtk_main_quit' : self.destroy, 
                                'on_next_BTN_clicked' : self.next_BTN_clicked,
                                'on_replay_BTN_clicked' : self.replay_BTN_clicked,
                                'on_add_tut_BTN_pressed' : self.add_tut_BTN_pressed,
                                'on_cancel_add_tut_BTN_pressed' : self.cancel_add_tut_BTN_pressed,
                                'on_add_add_tut_BTN_pressed' : self.add_add_tut_BTN_pressed,
                                'on_ok_BTN_pressed' : self.ok_BTN_pressed,
                                'on_about_menu_item_press' : self.about_menu_item_press,
                                'on_add_tut_menu_item_press' : self.add_tut_menu_item_press }
                                
        builder.connect_signals( signal_connections )
        
        self.window2 = builder.get_object("mainwindow2")
        self.window2.set_title("Daskalos")
        self.dialogbox = builder.get_object("dialogbox")
        self.filechooserdialog = builder.get_object('filechooserdialog')
        self.messagedialog = builder.get_object('messagedialog')
        self.aboutdialog = builder.get_object('aboutdialog')
        try:
            self.window2.set_icon_from_file("Daskalos.jpg")
        except Exception, e:
            pass
        
        treeview1 = builder.get_object("treeview1")
        self.treeview = treeview1
        self.treestore1 = self.init_treeview(treeview1)
        self.filenames = []
        self.menu_item_names = []
        self.get_list_items('', self.treestore1)                    #initially lists all tutorials
        treeview1.set_reorderable(False)
        
        self.description_label = builder.get_object("description_label")
        self.description_label.set_label('Select any tutorial from the list on the left or\n search in the searchbar above')
        self.tutorial_name_label = builder.get_object('tutorial_name_label')
        self.by_label = builder.get_object('by_label')
        self.approx_duration_label = builder.get_object('approx_duration_label')
        self.author_name_label = builder.get_object('author_name_label')
        self.duration_label = builder.get_object('duration_label')
        self.dialog_description_label = builder.get_object('dialog_description_label')
        
        self.stop_BTN = builder.get_object('stop_BTN')
        self.start_tut_BTN = builder.get_object('start_tut_BTN')
        self.next_BTN = builder.get_object('next_BTN')
        self.replay_BTN = builder.get_object('replay_BTN')
        
        self.screenshot = builder.get_object('screenshot')
        try :
            screenshot_path = self.images_path + 'daskalos_opening.png'
            self.screenshot.set_from_file(screenshot_path)
        except Exception, e:
            print 'Could not get Daskalos_opening.png image'
                
        searchbar = builder.get_object('searchbar')
        self.window2.show_all()
        self.start_tut_BTN.hide()
        self.by_label.hide()
        self.approx_duration_label.hide()
        self.tutorial_name_label.hide()

        raw_input("Press any key to quit")
        
    def init_treeview(self, treeview1):
        """
            This function initializes the treeview by defining the columns,
            etc and returns the treestore defined.
        """
        cell0 = gtk.CellRendererText()
        col0 = gtk.TreeViewColumn("   Tutorials", cell0, text = 0)
        treeview1.append_column(col0)
        
        treestore = gtk.TreeStore(str)
        self.detailed_tut = treestore.append(None, ['Detailed Tutorials'])
        self.tmt_tut = treestore.append(None, ['Take-me-there Tutorials'])
        liststore = gtk.ListStore( gobject.TYPE_STRING)
        treeview1.set_model(treestore)
        
        return treestore
        
    def get_list_items(self, substring, treestore):
        """
            This function gets the list items every time someone searches.
            It searches the tutorials directory and checks if the searchword
            is there in the header or Description of tutorial file. 
        """
        sys.path.append(self.tutorial_path)
        for filename in os.listdir(self.tutorial_path):
            (shortname, extension) = os.path.splitext(filename)
            if (extension == '.py'):
                try:
                	module = __import__(shortname)
                except Exception, e:
                	print 'Error while importing ', shortname
                try:
                    if((substring in module.tutorial.header.lower()) or (substring in module.tutorial.tags.lower())):
                        treestore.append(self.detailed_tut, [module.tutorial.header])
                        self.filenames.append(shortname)
                except Exception, e:
                    pass
        try :
            module = __import__('observer')
            for key in module.observer.dictionary.keys():
                if(substring in module.observer.dictionary[key][1].lower()):
                    treestore.append(self.tmt_tut, [key])
                    self.menu_item_names.append(key)
        except Exception :
            pass
        self.treeview.expand_all()
       
    def start_tut_BTN_button_press_event(self, data1, data2):
        """
            Called when start tutorial button is pressed in window2
        """
        if (self.start_tut_BTN.get_label() == 'Start Tutorial') :
            try :
                daskalos_ui_path = os.path.join(os.path.expandvars("$DSK_HOME"), 'src/ui/')
                sys.path.append(daskalos_ui_path)
                module = __import__('daskalos_dialogbox')
                module.dialogboxUI.mainwindow_start_tut_BTN(self)
            except Exception, e:
                print 'Could not import daskalos_dialogbox.py '
        else :
            try :
                module = __import__('observer')
                menu_list = module.observer.dictionary[self.selected_menu_item_name][0]
                time.sleep(1)
                module.observer.openWindowFromMenu(menu_list)
            except Exception :
                pass
                
    def run_tutorial(self, data1, data2):                
        #used it to debug things can be used to add some feature later if possible
        pass
        
    
    def cursor_changed(self, treeview):
        """
            This function is called when one among the list is chosen.It then goes
            to the corresponding file and extracts the descripton from that file and 
            gets the respective screenshot also .
        """
        if treeview.get_cursor()[0][0] == 0:
            try :
                self.selected_filename = self.filenames[treeview.get_cursor()[0][1]]
                module = __import__(self.selected_filename)         #should include a try here
                self.description_label.set_label(module.tutorial.Description)
                self.tutorial_name_label.set_label(module.tutorial.header)
                self.by_label.show()
                self.approx_duration_label.show()
                self.tutorial_name_label.show()
                try:
                    self.author_name_label.set_label(module.tutorial.Author)
                    self.duration_label.set_label(module.tutorial.duration)
                    self.start_tut_BTN.show()
                    self.start_tut_BTN.set_label('Start Tutorial')
                except Exception, e:
                    pass
                try :
                    self.screenshot.show()
                    screenshot_path = self.images_path + self.selected_filename + '_scaled.png'  
                    self.screenshot.set_from_file(screenshot_path)
                except Exception, e:
                    pass
            except Exception, e:
                print 'Error while importing when cursor changed'
        else:
            self.selected_menu_item_name = self.menu_item_names[(treeview.get_cursor()[0][1])]
            module = __import__('observer')
            try :
                self.description_label.set_label(module.observer.dictionary[self.selected_menu_item_name][1])
                screenshot_path = self.images_path + 'daskalos_opening.png'  
                self.screenshot.hide()
                self.author_name_label.set_label('')
                self.duration_label.set_label('')
                self.start_tut_BTN.show()
                self.start_tut_BTN.set_label('Take Me There')
            except Exception :
                pass
        
    def searchbar_changed(self, data):
        """
            This function is called when searchbar is changed in window2.
            The function clears the list first and then calls a
            function to get list items.
        """
        self.treestore1.remove(self.detailed_tut)
        self.treestore1.remove(self.tmt_tut)
        self.detailed_tut = self.treestore1.append(None, ['Detailed Tutorials'])
        self.tmt_tut = self.treestore1.append(None, ['Take-me-there Tutorials'])
        self.filenames = []
        self.menu_item_names = []
        self.get_list_items(data.get_text().lower(), self.treestore1)
            
    def on_stop_BTN_pressed(self, data = None):
        """
            Called when the stop button is pressed in dialog box.
        """
        self.dialogbox.hide()
        self.window2.show_all()
        self.stop_BTN.set_label('Stop')
        self.next_BTN.show()
        self.dialog_description_label.set_label('')
    
    def next_BTN_clicked(self, data = None):
        """
            When the next button is pressed in the dialog box this function is called
            It checks if there is a next.If it is not there it asks the user to press
            return
        """
        #try :
        daskalos_ui_path = os.path.join(os.path.expandvars("$DSK_HOME"), 'src/ui/')
        sys.path.append(daskalos_ui_path)
        module = __import__('daskalos_dialogbox')
        module.dialogboxUI.dialogbox_next_BTN_clicked(self)
        #except Exception, e:
        #    print 'Could not import daskalos_dialogbox.py '
        
    def replay_BTN_clicked(self,data = None):
        """
            When the replay button is pressed in dialogbox this function is called.
        """
        daskalos_ui_path = os.path.join(os.path.expandvars("$DSK_HOME"), 'src/ui/')
        sys.path.append(daskalos_ui_path)
        module = __import__('daskalos_dialogbox')
        module.dialogboxUI.dialogbox_replay_BTN_clicked(self)
        
    def destroy(self,widget, data = None):
    	print 'Quitting'
        gtk.main_quit()

    def add_tut_BTN_pressed(self, data = None):
        self.filechooserdialog.show()
        
    def add_tut_menu_item_press(self, data1 = None, data2 = None):
        self.filechooserdialog.show()
        
    def add_add_tut_BTN_pressed(self, data = None):
        complete_filename = self.filechooserdialog.get_filename()
        ( file_with_location, extension) = os.path.splitext(complete_filename)
        if (extension == '.py'):
            command = 'cp ' + complete_filename + ' ' + os.path.join(os.path.expandvars("$DSK_HOME"), 'src/tutorials/',os.path.basename(complete_filename))
            os.system(command)
        else :
            self.messagedialog.show()
        
    def cancel_add_tut_BTN_pressed(self, data = None):
        self.filechooserdialog.hide()
    
    def ok_BTN_pressed(self, data = None):
        self.messagedialog.hide()
    
    def about_menu_item_press(self, data1 =None, data2 = None):
        self.aboutdialog.run()
        self.aboutdialog.hide()       

        
    
daskalosUI = DaskalosUI()
    	
if __name__ == "__main__":
    daskalosUI.main()

