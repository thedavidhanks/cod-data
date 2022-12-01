import json
from os import system, name
from time import sleep
from cod_api import API, platforms
from dotenv import dotenv_values

config = dotenv_values(".env")

DEFAULT_GAMER_TAG="LordKeldrin#1771"
SSO_TOKEN = config['SSO_TOKEN']

# Constants
PF_BATTLENET = platforms.Battlenet
PF_ACTIVISIION = platforms.Activision
PF_PLAYSTATION = platforms.PSN
PF_STEAM = platforms.Steam
PF_UNO = platforms.Uno
PF_XBOX = platforms.XBOX

def clear():
    sleep(1)
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# initiating the API class & login in with sso TOKEN
api = API()
api.login(SSO_TOKEN)

## START User Input
clear()

# Request Gametag
print('What gamer would you like to review? (enter for default)')
usersGamerTag = input()
clear()

queryGamerTag = DEFAULT_GAMER_TAG if usersGamerTag == '' else usersGamerTag

# Request Platform
print('What platform is the gamer on? ')
print(' 1. Activision \n 2. Battlenet \n 3. Playstation \n 4. Steam \n 5. Uno \n 6. Xbox')
selectedPlatformNo = input().strip()
clear()
selectedPlatformNo = selectedPlatformNo[0]
match selectedPlatformNo:
    case '1':
        selectedPlatform = PF_ACTIVISIION
    case '2':
        selectedPlatform = PF_BATTLENET
    case '3':
        selectedPlatform = PF_PLAYSTATION
    case '4':
        selectedPlatform = PF_STEAM
    case '5':
        selectedPlatform = PF_UNO
    case '6':
        selectedPlatform = PF_XBOX
    case _:
        selectedPlatform = PF_BATTLENET
            
# retrieving combat history
# profile = api.Warzone.fullData(platforms.Battlenet, "LordKeldrin#1771") # returns data of type dict
profile = api.Warzone.fullData(platforms.Battlenet, queryGamerTag)
playerOnPlatform = queryGamerTag + ' on '+selectedPlatform.name
if(len(profile) > 0):
    print('Data found for '+ playerOnPlatform)
    print('Would you like to: \n1. Print results \n2. Save to file')
    printOrFile = input().strip()
    clear()
    printOrFileNum = printOrFile[0]
    if printOrFile == '2':
        filePrefix = input('Specify a filename: ')
        fileName = filePrefix+'.json' if len(filePrefix) > 0 else 'result.json'
        with open(fileName, 'w') as fp:
            json.dump(profile, fp, indent=4)
        print('data written to '+fileName)
    else:
        print(json.dumps(profile, indent=4))
else:
    print('No data found for '+playerOnPlatform)

# weaponInfo = profile["data"]["lifetime"]["itemData"]

# print(api.Warzone2.__doc__) # Prints the help info for getting warzone2 data.  See https://github.com/TodoLodo/cod-python-api#warzone2
