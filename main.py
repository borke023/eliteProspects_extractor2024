# []****************************[]
# ||                            ||
# ||   made by borke and toma   ||
# ||                            ||
# []****************************[]



import requests
import json
import os

def load_players():
    
    with open('players_input.txt', 'r', encoding='utf-8') as file:
        players = file.readlines()
        
    clean = []
    
    for player in players:
        clean.append(player.split('-')[1].strip())
        
    return clean

def save_file(data):
    
    info = ''

    for player in data:
        if player['position'] == 'Staff':
            continue
        else:
            info += f"{player['age']} - {player['countryName']} - {player['fullname']} - {player['id']}\n"

    path = 'players_output.txt'
    if os.path.exists(path):
        pass
    else:
        with open('players_output.txt', 'w', encoding='utf-8') as file:
            file.write('AGE | COUNTRY | NAME | ID\n')
    
    with open('players_output.txt', 'a', encoding='utf-8') as file:
        file.write(info)
    
def main():
    
    player_names = load_players()
    session = requests.Session()
    
    try:
        
        for count, player in enumerate(player_names):
            
            url = 'https://autocomplete.eliteprospects.com/all'
            
            params = {
                'q': player,
                'hideNotActiveLeagues': 1,
            }
            
            res = session.get(url, params=params)
            #print(res.json())
            save_file(res.json())
            
            # Used for progress bar
            os.system('cls') 
            print(f"Done: {count + 1}/{len(player_names)}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        session.close()
        return
    
    
if __name__ == '__main__':
    main()