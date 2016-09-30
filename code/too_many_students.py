# Created by: Matthew Lourenco
# Created on: 30 Sept 2016
# This is a program that creates a movable image

import ui

def check_touch_up_inside(sender):
    #check for number of students
    
    numberofstudents = int(view['guess_textfield'].text)
    if int(numberofstudents) > 30:
        view['answer_label'].text = 'too many students!'

view = ui.load_view()
view.present('full_screen')
