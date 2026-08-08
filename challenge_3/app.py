'''Build a User Configuration Manager'''

# # Create a dictionary named test_settings to store some user configuration preferences.

test_settings = {
    'theme': 'dark', 
    'notifications': 'enabled', 
    'volume': 'high',
}


# # You should define a function named view_settings with one parameter representing a dictionary of settings.

def view_settings(current_settings = {}):
    if not current_settings:  # Return No settings available. if the given dictionary of settings is empty.
        return "No settings available."


print(view_settings())