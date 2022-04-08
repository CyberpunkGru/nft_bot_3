import requests
from datetime import datetime
def sendWebhook(project, price,website,discord,twitter,datentime,type):
    url = 'https://discord.com/api/webhooks/890293627908157450/dNzEw5Ku6j_KeZaT2UL1Qqi_ZeuBVB5xJRX4JW1M93404rPS7RTYmsbuTYlXWQy_VGxY'
    data = {}
    if website is None:
        website = 'None'
    if discord is None:
        discord = 'None'
    if twitter is None:
        twitter = 'None'
    #print(project, price,website,discord,twitter,type)
    desc = f'{project} is dropping this week !!'
    type_field = {
        'name' : 'TYPE',
        'value' : type,
        'inline' : True
    }
    price_field = {
        'name' : 'PRICE',
        'value' : f'{price}',
        'inline' : True
    }
    website_field = {
        'name' : 'WEBSITE',
        'value' : website,
        'inline' : True
    }
    discord_field = {
        'name' : 'DISCORD',
        'value' : discord,
        'inline' : True
    }
    twitter_field = {
        'name' : 'TWITTER',
        'value' : f'[@{twitter}](https://twitter.com/{twitter})',
        'inline' : True
    }
    date_time_field = {
        'name' : 'DATE:',
        'value' : datentime,
        'inline' : True
    }
    
    data["embeds"] = [
        {
            "description" : desc,
            "title" : 'New Collection Drop Details',
            'fields' : [
                type_field , price_field ,date_time_field, website_field,discord_field,twitter_field        
            ]
        }
    ]
    result = requests.post(url , json= data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

