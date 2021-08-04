#import requests
import json
import random

url = 'https://zccpbzendeskco-ophelp.zendesk.com/api/v2/tickets/'           

#function to request tickets from API
#kept getting can not authenticate error 
#def request(url):
#    r = requests.get(url)
#    return r.json()

# to display a one ticket oneticketurl = rand
# def single_request(url,oneticketurl) :
#     sr = request.get(url,oneticketurl)
#     return sr.json()
           

ticketsFile = open('tickets.json','r')
data = ticketsFile.read()

#if request url worked -> tickets = request(url)
# single ticket -> stickets = single_request(url,oneticketurl)

tickets = json.loads(data)
list=tickets['tickets']

#displays all tickets
def parse_all(response):
    for i in response['tickets']:
        print()
        print("requesterID:",i['requester_id'], " ", "Subject:" ,i['subject'])
        #print(i['description'])

#displays one random ticket
def parse_one(response):
    rand = random.randint(0, 99)
    print()
    print("requesterID:",response[rand].get("requester_id"))
    print("subject:",response[rand].get("subject"))
    print("description:",response[rand].get("description"))

#display menu function
def menu():
    print("[1] Print all ticket")
    print("[2] Print one ticket")
    print("[0] Quit")

menu()
uInput = int(input("Pick a option:"))

# loops users input unit user chooses 0
while uInput != 0:
    if uInput == 1:
        parse_all(tickets)

    elif uInput == 2:
        parse_one(list)

    else:
        print("Pick a valid option ")

    print()
    menu()
    uInput = int(input("Pick a option: "))






