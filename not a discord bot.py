import requests, random, string, json

def rand_user(length):
   return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))

get_user = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1').json()
get_user_resp = get_user[0]

user = get_user_resp.split("@")[0]
domain = get_user_resp.split("@")[1]

currentuserfull = f"{user}@{domain}"
print(f'Your new email is {currentuserfull}')

#while True:
    #check_mail = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}')
check_mail = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login=alectest&domain=1secmail.com').json()
for msg in check_mail:
    current_msg_id = msg["id"]
    #msg_id_details = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={current_msg_id}')
    msg_id_details = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login=alectest&domain=1secmail.com&id={current_msg_id}').json()
    _from = msg_id_details['from']
    subject = msg_id_details['subject']
    txtbody = msg_id_details['textBody']
    print(f'New message from {_from}: {subject} {txtbody} ')

check_mail_id = check_mail[0]['id']
print(check_mail_id) 
