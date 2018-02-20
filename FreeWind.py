import json
import sys
from pprint import pprint
inFile = sys.argv[1]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Welcome to FreeWind.")

with open(inFile) as data_file:
    data = json.load(data_file)

with open('settings.json') as settings_file:
    settings = json.load(settings_file)

units = data["units"]
#P = f * Vk**2 * Ch * Cs

#f is a constant that depends on the units
if units == "N":
    print("Units set to " + units)
    f = 0.611
elif units == "kgf":
    print("Units set to " + units)
    f = 0.0623
elif units == "lbf":
    print("Units set to " + units)
    f = 0.00338
elif units ==  "":
    print(bcolors.WARNING + "Warning, no units specified. Defaulting to pound force.")
    f = 0.00338
else:
    print(bcolors.FAIL + "You specified units of " + units + " but units must be one of these: " + ','.join(settings["availableUnits"]))
    sys.exit("Error in input, Exiting...")
