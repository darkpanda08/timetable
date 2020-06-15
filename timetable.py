import requests
import json
import datetime


def lambda_handler(event=None, context=None):
    day = datetime.datetime.today().weekday()
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today_day = days_list[day]

    Monday = ["Subject 1,", "Subject 2,", "Subject 3"]
    Tuesday = ["Subject 1,", "Subject 2,", "Subject 3"]
    Wednesday = ["Subject 1,", "Subject 2,", "Subject 3"]
    Thursday = ["Subject 1,", "Subject 2,", "Subject 3"]
    Friday = ["Subject 1,", "Subject 2,", "Subject 3"]
    Saturday = ["Subject 1,", "Subject 2,", "Subject 3"]

    webhook_url = 'Your-Slack-Webhook-URL'
    
    send_data = "Good Morning Vineet!! :smile:\nToday it's " + days_list[day] + "\n\nTimetable is :"
    
    def webhook_send():
        response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    
    
    if (day == 0):
        for i in range(len(Monday)):
            send_data = send_data + " " + Monday[i]

        data = { 'text': send_data }


    if (day == 1):
        for i in range(len(Tuesday)):
            send_data = send_data + " " + Tuesday[i]
    
        data = { 'text': send_data }
            
    
    if (day == 2):
        for i in range(len(Wednesday)):
            send_data = send_data + " " + Wednesday[i]
    
        data = { 'text': send_data }
    
    
    if (day == 3):
        for i in range(len(Thursday)):
            send_data = send_data + " " + Thursday[i]
    
        data = { 'text': send_data }
    
    
    if (day == 4):
        for i in range(len(Friday)):
            send_data = send_data + " " + Friday[i]
    
        data = { 'text': send_data }
    
    
    if (day == 5):
        for i in range(len(Saturday)):
            send_data = send_data + " " + Saturday[i]

        data = { 'text': send_data }
    
    
    if (day == 6):
        data = { 'text': 'Today is Sunday :smile: \nNo classes today. Enjoy!!!!' }
            
    
    webhook_send()
  
