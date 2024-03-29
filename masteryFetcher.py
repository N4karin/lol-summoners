#! /usr/bin/env python3

import requests
import json

all_champion_id = {
        1: "Annie",
        2: "Olaf",
        3: "Galio",
        4: "Twisted Fate",
        5: "Xin Zhao",
        6: "Urgot",
        7: "LeBlanc",
        8: "Vladimir",
        9: "Fiddlesticks",
        10: "Kayle",
        11: "Master Yi",
        12: "Alistar",
        13: "Ryze",
        14: "Sion",
        15: "Sivir",
        16: "Soraka",
        17: "Teemo",
        18: "Tristana",
        19: "Warwick",
        20: "Nunu",
        21: "Miss Fortune",
        22: "Ashe",
        23: "Tryndamere",
        24: "Jax",
        25: "Morgana",
        26: "Zilean",
        27: "Singed",
        28: "Evelynn",
        29: "Twitch",
        30: "Karthus",
        31: "Cho'Gath",
        32: "Amumu",
        33: "Rammus",
        34: "Anivia",
        35: "Shaco",
        36: "Dr.Mundo",
        37: "Sona",
        38: "Kassadin",
        39: "Irelia",
        40: "Janna",
        41: "Gangplank",
        42: "Corki",
        43: "Karma",
        44: "Taric",
        45: "Veigar",
        48: "Trundle",
        50: "Swain",
        51: "Caitlyn",
        53: "Blitzcrank",
        54: "Malphite",
        55: "Katarina",
        56: "Nocturne",
        57: "Maokai",
        58: "Renekton",
        59: "Jarvan IV",
        60: "Elise",
        61: "Orianna",
        62: "Wukong",
        63: "Brand",
        64: "Lee Sin",
        67: "Vayne",
        68: "Rumble",
        69: "Cassiopeia",
        72: "Skarner",
        74: "Heimerdinger",
        75: "Nasus",
        76: "Nidalee",
        77: "Udyr",
        78: "Poppy",
        79: "Gragas",
        80: "Pantheon",
        81: "Ezreal",
        82: "Mordekaiser",
        83: "Yorick",
        84: "Akali",
        85: "Kennen",
        86: "Garen",
        89: "Leona",
        90: "Malzahar",
        91: "Talon",
        92: "Riven",
        96: "Kog'Maw",
        98: "Shen",
        99: "Lux",
        101: "Xerath",
        102: "Shyvana",
        103: "Ahri",
        104: "Graves",
        105: "Fizz",
        106: "Volibear",
        107: "Rengar",
        110: "Varus",
        111: "Nautilus",
        112: "Viktor",
        113: "Sejuani",
        114: "Fiora",
        115: "Ziggs",
        117: "Lulu",
        119: "Draven",
        120: "Hecarim",
        121: "Kha'Zix",
        122: "Darius",
        126: "Jayce",
        127: "Lissandra",
        131: "Diana",
        133: "Quinn",
        134: "Syndra",
        136: "Aurelion Sol",
        141: "Kayn",
        142: "Zoe",
        143: "Zyra",
        145: "Kai'sa",
        150: "Gnar",
        154: "Zac",
        157: "Yasuo",
        161: "Vel'Koz",
        163: "Taliyah",
        164: "Camille",
        201: "Braum",
        202: "Jhin",
        203: "Kindred",
        222: "Jinx",
        223: "Tahm Kench",
        236: "Lucian",
        238: "Zed",
        240: "Kled",
        245: "Ekko",
        246: "Qiyana",
        254: "Vi",
        266: "Aatrox",
        267: "Nami",
        268: "Azir",
        350: "Yuumi",
        412: "Thresh",
        420: "Illaoi",
        421: "Rek'Sai",
        427: "Ivern",
        429: "Kalista",
        432: "Bard",
        497: "Rakan",
        498: "Xayah",
        516: "Ornn",
        517: "Sylas",
        518: "Neeko",
        555: "Pyke",
}

serverList = {
        "euw": "euw1",
        "euwest": "euw1",
        "eu west": "euw1",
        "europe west": "euw1",
        "na": "na1",
        "north america": "na1",
        "kr": "kr",
        "korea": "kr",
        "jp": "jp1",
        "japan": "jp1",
        "brazil": "br1",
        "br": "br1",
        "oce": "oc1",
        "oceania": "oc1",
        "lan": "la1",
        "las": "la2",
        "ru": "ru",
        "russia": "ru",
        "turkey": "tr1",
        "tr": "tr1",
        "pbe": "pbe1",
}

api = "" # Fill this in
summoner = input('Please enter a summoner name\n')

serverInput = input('Please enter the region of the summoner name\n')
server = serverList.get(serverInput.lower())

if server is None:
        print("Server not found, please inspect input")
        exit()

summonerInfo = requests.get("https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner +
                            "?api_key=" + api)

if summonerInfo.status_code == 200:
    print('Summoner found')
    accountJSON = json.loads(summonerInfo.text)
    accountId = accountJSON["id"]
    print("Fetching Champion list...\n")
    mostPlayedChamps = requests.get("https://" + server +
                                    ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" +
                                    accountId + "?api_key=" + api)
    if mostPlayedChamps.status_code == 200:
        champList = json.loads(mostPlayedChamps.text)
        for i in range (10):
                try:
                        print('{:<13s}{:>7s}'.format(all_champion_id.get(champList[i]["championId"]),
                                                     f'{champList[i]["championPoints"]:,}'))
                except:
                        print("No more champions found")
                        break
    else:
        print("Error " + str(mostPlayedChamps.status_code))
else:
    print("Error " + str(summonerInfo.status_code) + "\nPlease check API key, summoner name and server")