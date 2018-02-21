import json
import sys
from pprint import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + "Welcome to FreeWind." + bcolors.ENDC)

try:
    inFile = sys.argv[1]
except:
    sys.exit("No input file specified...")
try:
    outFile = sys.argv[2]
except IndexError:
    print(bcolors.WARNING + "No output filename specified, using default outfile.txt" + bcolors.ENDC)
    outFilie = 'outfile.txt'

with open(inFile) as data_file:
    data = json.load(data_file)

with open('settings.json') as settings_file:
    settings = json.load(settings_file)

units = data["units"]
#P = f * Vk**2 * Ch * Cs

#f is a constant that depends on the units
if units == "N":
    print(bcolors.OKBLUE + "Units set to " + units + bcolors.ENDC)
    f = 0.611
    chUnits = "meters"
elif units == "kgf":
    print(bcolors.OKBLUE + "Units set to " + units + bcolors.ENDC)
    f = 0.0623
    chUnits = "meters"
elif units == "lbf":
    print(bcolors.OKBLUE + "Units set to " + units + bcolors.ENDC)
    f = 0.00338
    chUnits = "feet"
elif units ==  "":
    print(bcolors.WARNING + "Warning, no units specified. Defaulting to pound force." + bcolors.ENDC)
    f = 0.00338
    chUnits = "feet"
else:
    print(bcolors.FAIL + "You specified units of " + units + " but units must be one of these: " + ','.join(settings["availableUnits"])+ bcolors.ENDC)
    sys.exit("Error in units input, Exiting...")

speedUnits = data["speedUnits"]

#TODO:Change so that you can use knots with metric units and the program will convert for you

if speedUnits == "m/s":
    if units == "lbf":
        print(bcolors.FAIL + "Units mismatch!" + bcolors.ENDC)
        sys.exit("Error in input, Exiting...")
    elif units == "m/s":
        print(bcolors.OKBLUE + "Wind speed units set to " + speedUnits + bcolors.ENDC)
elif speedUnits == "kn":
    if units != "lbf":
        print(bcolors.FAIL + "Units mismatch!" + bcolors.ENDC)
        sys.exit("Error in input, Exiting..." + bcolors.ENDC)
    elif units == "lbf":
        print(bcolors.OKBLUE + "Wind speed units set to " + speedUnits + bcolors.ENDC)
else:
    print(bcolors.FAIL + "You specified wind speed units of " + speedUnits + " but it must be one of these: " + ','.join(settings["availableSpeedUnits"]) + bcolors.ENDC)
    sys.exit("Error in speed input, Exiting...")

print("Program will use the following wind speeds " + ','.join(str(x) for x in data["speeds"]))

headingIncrement = data["headingIncrement"]

if headingIncrement < 0:
    print(bcolors.FAIL + "Heading increment cannot be less than zero." + bcolors.ENDC)
    sys.exit("Error in heading input, Exiting...")
elif headingIncrement < 1:
    print(bcolors.WARNING + "Warning, heading increment is less than one degree." + bcolors.ENDC)
    ans = input("Continue (y/n)?:").lower()
    if ans == "n":
        sys.exit("Error in heading input, Exiting...")
    elif ans == "y":
        print("Continuing with small angle heading increment...")
elif headingIncrement > 360:
    print(bcolors.FAIL + "Heading increment cannot be greater than 360" + bcolors.ENDC)
    sys.exit("Error in heading input, Exiting...")
else:
    print("Heading increment set as " + str(headingIncrement))

headings = [0]
heading = 0
while heading < 360:
    heading = heading + headingIncrement
    if heading != 360 and heading < 360:
        headings.append(heading)
print("Program will use the following headings: " + ', '.join(str(x) for x in headings))

print(bcolors.OKBLUE + "Accessing tabular values of height coefficient assuming height units are: " + chUnits + bcolors.ENDC)

if chUnits == "feet":
    ch = settings["ch-feet"]
elif chUnits == "meters":
    ch = settings["ch-meters"]

pprint(ch)
print(bcolors.OKBLUE + "Please make sure your model units match." + bcolors.ENDC)
input("Review the above information and press enter to begin reading model data...")

#TODO: Read in model data from json file to python class
pprint(data["model"])
#TODO: Output a 3d model of the data


input("Review the above information and press enter to begin calculating wind speeds...")
for speed in data["speeds"]:
    print("****************"+str(speed)+ " " + speedUnits +"*********************")
    for heading in headings:
        #for part in model:
            #TODO: Calculate projected area for each object at this heading and determine
        print("Wind force is XXX at " + str(heading) + " degrees in " + str(speed) + " " + speedUnits)

#TODO: Write output to file in whatever format required

print("Finished calculating with no errors, writing output file...")

if os.path.isfile(outFile) then:
    outAns = input("Output file alread exists, overwright? (y/n)").lower()
    if outAns == "y":
        print("Overwriting existing file.")
    elif outAns == "n":
        outFile = input("PLease enter a new output file name: ")
    else:
