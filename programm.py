def print_menu():
    print('\nMain Menu\n'
          '---------\n'
          '0 - Convert temperature\n'
          '1 - Process a new data file\n'
          '2 - Choose units\n'
          '3 - Edit room filter\n'
          '4 - Show summary statistics\n'
          '5 - Show temperature by date and time\n'
          '6 - Show histogram of temperatures\n'
          '7 - Quit\n'
          '')

print_menu()

def convert_units(celsius_value, units):
    if units == 0:
        return celsius_value
    if units == 1:
        return celsius_value * 1.8 + 32
    if units == 2:
        return celsius_value + 273.15
