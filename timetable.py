import requests
import json
import datetime

day = datetime.datetime.today().weekday()
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today_day = days_list[day]
print(today_day)


Monday = ["Artificial Intelligence,", "Power Electronics,", "Signals & Systems,", "Microcontrollers,", "Placement Training"]
Tuesday = ["Signals & Systems,", "Artificial Intelligence,", "Power Electronics,", "Management & Enterpreneurship,", "PE Lab"]
Wednesday = ["Power Electronics,", "Management & Enterpreneurship,", "Microcontrollers Lab"]
Thursday = ["Estimation & Costing,", "Microcontrollers,", "Artificial Intelligence,", "Signals & Systems"]
Friday = ["Power Electronics,", "Microcontrollers,", "Management & Enterpreneurship,", "Estimation & Costing"]
Saturday = ["Estimation & Costing,", "Signals & Systems,", "Microcontrollers,", "Management & Enterpreneurship"]


wekbook_url = 'https://hooks.slack.com/services/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'

send_data = "Good Morning Vineet!! \nToday it's " + days_list[day] + "\n\nTimetable is :"

def webhook_send():
    response = requests.post(wekbook_url, data=json.dumps(
        data), headers={'Content-Type': 'application/json'})

    if (response.status_code != 200):
        print('Response: ' + str(response.text))
        print('Response code: ' + str(response.status_code))

    

if (day == 0):
    for i in range(5):
        send_data = send_data + " " + Monday[i]
        
    data = {
        'text': send_data,
        'username': 'My Home',
    }
    webhook_send()


if (day == 1):
    for i in range(5):
        send_data = send_data + " " + Tuesday[i]

    data = {
        'text': send_data,
        'username': 'My Home',
    }
    webhook_send()

if (day == 2):
    for i in range(4):
        send_data = send_data + " " + Wednesday[i]

    data = {
        'text': send_data,
        'username': 'My Home',
    }
    webhook_send()


if (day == 3):
    for i in range(4):
        send_data = send_data + " " + Thursday[i]

    data = {
        'text': send_data,
        'username': 'My Home',
    }
    webhook_send()

if (day == 4):
    for i in range(4):
        send_data = send_data + " " + Friday[i]

    data = {
        'text': send_data,
        'username': 'My Home',
    }
    webhook_send()

if (day == 5):
    for i in range(4):
        send_data = send_data + " " + Saturday[i]

    data = {
        'text': send_data,
        'username': 'My Home',
    }
    webhook_send()

if (day == 6):
    data = {
        'text': 'No classes today. Enjoy!!!!',
        'username': 'My Home',
    }
    webhook_send()
