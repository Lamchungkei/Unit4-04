# Created by: Kay Lin
# Created on: 7th-Nov-2017
# Created for: ICS3U
# This program displays your mark level converts to percentage

def percentage(level):
    # enter your level of grade and returns the middle percentage mark
    
    if level == '4+' :
       return 97.5
    
    elif level == '4' :
       return 90.5
    
    elif level == '4-' :
       return 83
    
    elif level == '3+':
       return 78
    
    elif level == '3':
       return 74.5
    
    elif level == '3-':
       return 71
    
    elif level == '2+':
       return 68
    
    elif level == '2':
       return 64.5
    
    elif level == '2-':
       return 61
    
    elif level == '1+':
       return 58
    
    elif level == '1':
       return 54.5
    
    elif level == '1-':
       return 51
    
    elif level == 'R':
       return 24.5
    
    else:
       return -1
    
# percentage function
level = raw_input('Enter your level of grade: ')
percentage_print = percentage(level)
print('Your percentage is ' + str(percentage_print))
