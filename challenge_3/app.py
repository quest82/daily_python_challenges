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

# # 