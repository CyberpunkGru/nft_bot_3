import time
from blackbox import get_data
from date_parser import parse_date
from webhook import sendWebhook
import datetime


enlisted_id = []


def begin():
    global enlisted_id
    try:
        cnt = 0 
        data = get_data()
        for objct in data: 
            try:
                #print(objct['Project'] , objct['Price'] , objct['Sale Date'],objct['Website'] , objct['Discord'],objct['TwitterId'] ,sep=' ')
                #print(objct['date'])
                Sale_date = (datetime.datetime.utcnow() + datetime.timedelta(hours = 8640)).date()
                Presale_date = (datetime.datetime.utcnow() + datetime.timedelta(hours = 8640)).date()
                try:
                    Sale_date = parse_date(objct['Sale Date'])
                except:
                    a = 1
                try:
                    Presale_date = parse_date(objct['Presale Date'])
                except:
                    b =1 
                current_date = (datetime.datetime.utcnow() - datetime.timedelta(hours = 5)).date()
                ahead_date = (datetime.datetime.utcnow() + datetime.timedelta(days = 7)).date()
               # print(current_date,Sale_date,Presale_date)
               
                if Presale_date >= current_date and Presale_date <=ahead_date:
                    if (objct , 'Presale') in enlisted_id:
                        continue
                    enlisted_id.append((objct,'Presale'))
                    print(objct['Project'])
                    try:
                        datentime = f'{str(Presale_date)}'
                        Project , Price , Website , Discord , Twitter = parse_data(objct)
                        sendWebhook(Project , Price , Website , Discord , Twitter,datentime,'Presale')
                        cnt = cnt + 1 
                        time.sleep(2)
                    except:
                        print("Error in sending webhook")
                if Sale_date >= current_date and Sale_date <=ahead_date:
                    if (objct , 'Sale') in enlisted_id:
                        continue
                    enlisted_id.append((objct,'Sale'))
                    print(objct['Project'])
                    datentime = f'{str(Sale_date)}'
                    #print(objct['Project'] , objct['Price'],objct['Website'] ,objct['Discord'],objct['TwitterId'])
                    try:
                        Project , Price , Website , Discord , Twitter = parse_data(objct)
                        sendWebhook(Project , Price , Website , Discord , Twitter,datentime,'Sale')
                        cnt = cnt + 1
                        time.sleep(2)
                    except:
                        print("Error in sending webhook")
                #print(date)
            except:
                print("error caught",objct['id'])
                continue
    except:
        print("Error in fetching rarity data ")
    print(cnt)


def parse_data(objct):
    Project = 'None'
    Price = 'Free'
    Website = 'None'
    Discord = 'None'
    Twitter = 'None'
    try:
        Project = objct['Project']
    except:
        a = 1
    try:
        Price = objct['Price']
    except:
        a = 1
    try:
        Website = objct['Website']
    except:
        a = 1
    try:
        Discord = objct['Discord']
    except:
        a = 1
    try:
        Twitter = objct['TwitterId']
    except:
        a = 1
    return Project , Price , Website , Discord , Twitter


    

