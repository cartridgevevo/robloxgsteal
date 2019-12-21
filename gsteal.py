import requests , random , threading , ctypes
import platform
import json

print('''
If you haven't, please configure your GSteal for Discord Webhooks
''')

print('''
Join the GSteal Discord Server - https://discord.gg/gwpYqdy
''')

print('''
GSteal - Owned and Emotional Support by Charge. GSteal by MrCorbie. Modified by ryuunosuke02420 and cartridgevevo
''')

thread_count = int(input('How many threads do you want? (500 is good for playing, 850 for maximum efficency) : '))
botstart_note = str(input('What customized note do you want on your embed? : '))

data = json.load(open('config.json', 'r'))

# Discord Webhooks - Connected to config.json
url = data['url']
url_failed = data['url_failed']
url_10ormode = data['url_10ormode']
# url_100member = data['url_100member'] - Hey there, you're peeking into the future of GSteal, fuck off

# Robux Configuration - Connected to config.json
lowrobux = data['lowrobux']


def sendmessage(webURL, groupID, name, memberCount, robux, description, date):
    data = {
        "username": "GSteal",
        "avatar_url": "https://cdn.discordapp.com/icons/585451780977065994/cddcc4cf0acf9b57c2654331fec153e9.png",
        "embeds": [
        {
            "author": {
            "name": "GSteal v1.2.1",
            "url": "",
            "icon_url": ""
        },
            "title": "Name: " + str(name),
            "color": random.randint(100000,500000),
            "fields": [
                 {
                "name": "Total Members",
                "value": str(memberCount) + " Members",
                "inline": True
            },
                 {
                "name": "Total R$",
                "value": str(robux),
                "inline": True
            },
            {
                "name": "Group Link",
                "value": 'https://www.roblox.com/groups/' + str(groupID),
                "inline": True
            },
            {
                "name": "System Running Code",
                "value": platform.system(),
                "inline": True
            },
            {
                "name": "Note by Bot Starter",
                "value": str(botstart_note),
                "inline": True
            },
            {
                "name": "Group Description",
                "value": str(description),
                "inline": True
            },
        ],
            "footer": {
             "text": "Made by MrCorbie & cartridgevevo | Owned by Charge ",
                         "icon_url": ""
            }
        }
	    ]
    }
    h = requests.post(webURL, json=data)

groups_valid = 0
groups_scanned = 0
robux = 0
groups_list = []
groups_removed = 0
def group_scanning():
    while True:
        try:
            global groups_valid
            global groups_scanned
            global robux
            global groups
            global groups_removed

            if platform.system() == 'Windows':
                ctypes.windll.kernel32.SetConsoleTitleW('GSteal | Total Checking : {}  | Groups Valid : {} | Groups Removed : {} | R$ Earned : {} | by MrCorbie & cartridgevevo | Owned by Charge'.format(groups_scanned,groups_valid,groups_removed,robux))
            groupID = random.randint(1,5901231)

            checking = requests.get('https://groups.roblox.com/v1/groups/{}'.format(groupID))
            currency = requests.get('https://economy.roblox.com/v1/groups/{}/currency'.format(groupID))

            groups_scanned += 1

            if checking.status_code != 200:
                continue
            else:
                if 'isLocked' in checking.json():
                    continue
                else:
                    if checking.json()['publicEntryAllowed'] == False or checking.json()['owner'] != None:
                        continue
                    else:

                        
                        if groupID not in groups_list:
                            groups_list.append(groupID)
                            groups_valid += 1
                        else:
                            groups_removed += 1
                            continue

                        if currency.status_code == 200 and currency.json()['robux'] > 0:
                            print('>> {} | Robux : {} | {}\n'.format(checking.json()['id'],currency.json()['robux'], currency.json()))
                            robux += currency.json()['robux']
                            with open('groups_robux.txt','a',encoding='UTF-8') as f:
                                f.write('{} | {} | {} | Robux : {}\n'.format(checking.json()['id'],checking.json()['name'],'https://www.roblox.com/groups/' + str(groupID) + 'a',currency.json()['robux']))
                            if currency.json()["robux"]<lowrobux:
                                sendmessage(url, checking.json()['id'], checking.json()['name'], checking.json()['memberCount'], currency.json()['robux'], checking.json()['description'], "26/05/2019")
                            else:
                                sendmessage(url_10ormode, checking.json()['id'], checking.json()['name'], checking.json()['memberCount'], currency.json()['robux'], checking.json()['description'], "26/05/2019")
                        else:
                            sendmessage(url_failed, checking.json()['id'], checking.json()['name'], checking.json()['memberCount'], 0, checking.json()['description'], "26/05/2019")
                            print('>> {} | No Owner | {}\n'.format(checking.json()['id'], checking.json()['name'], checking.json()['memberCount'], currency.json()))
                            with open('groups.txt','a',encoding='UTF-8') as f:
                                f.write('{} | {} | {} \n'.format(checking.json()['id'],checking.json()['name'] ,'https://www.roblox.com/groups/' + str(groupID) + '/a'))
        except Exception as e:
            print(e)


for x in range(thread_count):
    threading.Thread(target=group_scanning).start()