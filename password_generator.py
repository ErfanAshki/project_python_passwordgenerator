import random
import string
import os


settings = {
    'lower' : True , 
    'upper' : True , 
    'number' : True , 
    'symbol' : True , 
    'space' : False , 
    'length' : 10
}
MINIMUM_LENGTH = 6
MAXIMUM_LENGTH = 25


def clear_screen_and_welcome_message():
    os.system('cls')
    print('Welcome to password generate app :))')
    print('Enter your settings until we create a random password for you .')



def get_valid_options_for_settings(option, default):
    while True:
        user_setting = input(f"{option} include ? default is : {default} ."
                            " (y:yes - n:no - enter:default) ")

        if user_setting == '':
            return default
        
        if user_setting in ['y', 'n']:
            return user_setting == 'y'
        
        print('Invalid input , Please try again .')
        

def get_password_length(option, default):
    while True:
        user_input = input(f"Enter your length (password must be in range ({MINIMUM_LENGTH},{MAXIMUM_LENGTH})) :  "
                           f"default is = {default} . (enter:default) ")

        if user_input == '':
            return default
        
        if user_input.isdigit() :
            if  int(user_input) >= MINIMUM_LENGTH and  int(user_input) <= MAXIMUM_LENGTH:
                return int(user_input)
            print('Please enter a number in specific range . ')
        else:    
            print('Please enter a number .')


def get_settings_from_user(settings):
    
    for option, default in settings.items():
        if option != 'length': 
            user_choice = get_valid_options_for_settings(option , default)
            settings[option] = user_choice
        else:
            user_length = get_password_length(option, default)
            settings[option] = user_length
        
    return settings


def generate_random_chars(choices):
    choice = random.choice(choices)
    
    if choice == 'upper':
        return random.choice(string.ascii_uppercase)
    
    elif choice == 'lower':
        return random.choice(string.ascii_lowercase)
    
    elif choice == 'number':
        return random.choice(string.digits)
    
    elif choice == 'symbol': 
        return random.choice(string.punctuation)
    
    elif choice == 'space':
        return random.choice(string.whitespace)
    


def password_generate(settings):
    setting_choices = list(filter(lambda x : settings[x] , ['upper', 'lower', 'number', 'symbol', 'space']))
    
    password_length = settings['length']
    final_password = ''
    
    for pass_w in range(password_length):
        final_password += generate_random_chars(setting_choices)

    
    return final_password

def run():       
    clear_screen_and_welcome_message()
    print('-' * 20)
    get_settings_from_user(settings)
    print('-' * 20)
    print(f"Generated password : {password_generate(settings)}")
    

run()

