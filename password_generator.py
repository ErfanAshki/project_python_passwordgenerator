

settings = {
    'lower' : True , 
    'upper' : True , 
    'number' : True , 
    'symbol' : True , 
    'space' : False , 
    'length' : 10
}


def get_valid_options_for_settings(option, default):
    while True:
        user_setting = input(f"{option} include ? default is : {default} . (y:yes - n:no - enter:default) ")

        if user_setting == '':
            return default
        
        if user_setting in ['y', 'n']:
            return user_setting == 'y'
        
        print('Invalid input , Please try again .')


def get_settings_from_user(settings):
    
    for option, default in settings.items():
        if option != 'length': 
            user_choice = get_valid_options_for_settings(option , default)
            settings[option] = user_choice
            
        
    return settings

        
get_settings_from_user(settings)

print(settings)
