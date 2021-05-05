import json

print('''
GSteal Configuration - by cartridgevevo
''')

print('''
To share a group with all robux, enter 0 on the Robux amount question and put the same webhook on the configuration questions about the configured robux amounts.
''')

lowrobux = str(input('What Robux amount do you consider low? (to not set this up press 0) : '))
url = str(input('Which Discord Webhook URL are you using for groups with less then the configured low robux amount? : '))
url_10ormode = str(input('What Discord Webhook URL are you using for groups with more then the configured robux amount? : '))
url_failed = str(input('What Discord Webhook URL are you using for groups with no Robux? : '))
# url_100member = str(input("Which Discord Webhook URL are you using for groups with more then 100 members? : ")) - Hey there, you're peeking into the future of GSteal
 
config = {
    'lowrobux': str(lowrobux),
    'url': str(url),
    'url_failed': str(url_failed),
    'url_10ormode': str(url_10ormode)
#   'url_100member': str(url_100member) - Hey there, you're peeking into the future of GSteal
}
 
with open('config.json','w') as config_dumped :
    json.dump(config,config_dumped,indent = 4,sort_keys = True)

#   Configwrite.py by cartridgevevo.
#   All of this was written at 2am
#   I am gamer
