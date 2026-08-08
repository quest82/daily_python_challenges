'''Build a User Configuration Manager'''

# # Create a dictionary named test_settings to store some user configuration preferences.

test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high',
}

# # You should define a function named view_settings with one parameter representing a dictionary of settings.

def view_settings(current_settings = {}):
    if not current_settings:  # Checks if dictionary is empty
        return "No settings available."

    settings = f"Current User Settings:\n" # Runs if dictionary is populated
    for key, value in current_settings.items():
        settings += f"{key.capitalize()}: {value}\n"
    return settings

# print(view_settings(test_settings))

# # You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair

def add_setting (current_settings = {}, new_setting =('key', 'value')):
    key, value = new_setting[0].lower(), new_setting[1].lower()

    if key in current_settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    current_settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!."

# print(add_setting(test_settings, ('Brightness', '80%')))


