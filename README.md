## Getting started
    
    1. install cod-api  

        pip install -U cod-api

    2. Get an SSO token
    3. Udpate the .env-example with your SSO token
    4. Rename to .env
    5. run main `py main.py`

## COD-python API Reference   

[cod-python-api](https://github.com/TodoLodo/cod-python-api)  
  
  
### Methods for viewing Warzone 2 data
  
Warzone 2 class: A class to get players warzone 2 stats, warzone 2 combat history and specific warzone 2 match details:

    classCategory: game  
    gameId/gameTitle: mw or wz  
    gameType: wz2  


        Methods
        =======
        Sync
        ----
        fullData(platform:platforms, gamertag:str)
            returns player's game data of type dict

        combatHistory(platform:platforms, gamertag:str)
            returns player's combat history of type dict

        combatHistoryWithDate(platform:platforms, gamertag:str, start:int, end:int)
            returns player's combat history within the specified timeline of type dict

        breakdown(platform:platforms, gamertag:str)
            returns player's combat history breakdown of type dict

        breakdownWithDate(platform:platforms, gamertag:str, start:int, end:int)
                    returns player's combat history breakdown within the specified timeline of type dict

        seasonLoot(platform:platforms, gamertag:str)
            returns player's season loot

        mapList(platform:platforms)
            returns available maps and available modes for each

        matchInfo(platform:platforms, matchId:int)
                    returns details match details of type dict

        Async
        ----
        fullDataAsync(platform:platforms, gamertag:str)
            returns player's game data of type dict

        combatHistoryAsync(platform:platforms, gamertag:str)
            returns player's combat history of type dict

        combatHistoryWithDateAsync(platform:platforms, gamertag:str, start:int, end:int)
            returns player's combat history within the specified timeline of type dict

        breakdownAsync(platform:platforms, gamertag:str)
            returns player's combat history breakdown of type dict

        breakdownWithDateAsync(platform:platforms, gamertag:str, start:int, end:int)
                    returns player's combat history breakdown within the specified timeline of type dict

        seasonLootAsync(platform:platforms, gamertag:str)
            returns player's season loot

        mapListAsync(platform:platforms)
            returns available maps and available modes for each

        matchInfoAsync(platform:platforms, matchId:int)
                    returns details match details of type dict