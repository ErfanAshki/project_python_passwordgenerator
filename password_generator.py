

settings = {
    'lower' : True , 
    'upper' : True , 
    'number' : True , 
    'symbol' : True , 
    'space' : False , 
    'length' : 10
}

def get_settings_from_user(settings):
    
    for option, default in settings.items():
        if option != 'length': 
            while True:
                user_setting = input(f"{option} include ? default is : {default} . (y:yes - n:no) ")
                
                if user_setting in ['y', 'n']:
                    if user_setting == 'y':
                        settings[option] = True
                    else:
                        settings[option] = False
                    break
                else:
                    print('Invalid input , Please try again .')
        
    return settings
        
get_settings_from_user(settings)

print(settings)
