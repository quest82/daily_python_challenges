'''Build a User Configuration Manager'''

# # Create a dictionary named test_settings to store some user configuration preferences.

test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high',
}

# # Convert key and value of a tuple to a list
def to_lowercase(tup=()):
        return [x.lower() for x in tup]

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
    key, value = to_lowercase(new_setting)

    if key in current_settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    current_settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!."

print(add_setting(test_settings, ('Brightness', '80%')))

# # You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

def update_setting(current_settings = {}, new_setting =('key', 'value')):
    key, value = to_lowercase(new_setting)

    # print(key, value)

            # update_setting function should:
            # Convert the key and value to lowercase.
            # If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
            # If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
            # The messages returned should have the key and value in lowercase.
# update_setting(test_settings, ('Brightness', '80%'))

