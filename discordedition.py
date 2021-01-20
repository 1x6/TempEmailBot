import discord
from discord.ext import commands, tasks
import random, requests, string, json

# i provide absolutely zero notes - i just dont do that
# please dont skid its not worth it

client = commands.Bot(command_prefix='~')

def rand_code(length):
   return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))

@client.command()
async def new(ctx):
    get_user = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1').json()
    get_user_resp = get_user[0]

    user = get_user_resp.split("@")[0]
    domain = get_user_resp.split("@")[1]

    currentuserfull = f"{user}@{domain}"
    current_auth_code = rand_code(7)

    f = open(f"E:\Coding\Discord Bot\Disposable Email Bot\{ctx.message.author.id}.txt", "w")
    f.write(f"{current_auth_code}|{currentuserfull}")
    f.close()

    await ctx.author.send(f'Your new email is `{currentuserfull}`. To check messages, use code `{current_auth_code}`.')

@client.command()
async def check(ctx, code):
    f = open(f"E:\Coding\Discord Bot\Disposable Email Bot\{ctx.message.author.id}.txt", "r")
    fcontents = f.read()
    auth_code = fcontents.split("|")[0]
    email = fcontents.split("|")[1]

    if code == auth_code:
        user = email.split("@")[0]
        domain = email.split("@")[1]

        check_mail = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}').json()
        for msg in check_mail:
            current_msg_id = msg["id"]
            msg_id_details = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={user}&domain={domain}&id={current_msg_id}').json()
            _from = msg_id_details['from']
            subject = msg_id_details['subject']
            txtbody = msg_id_details['textBody']
            await ctx.author.send(f'New message from `{_from}`: `{subject}` ```{txtbody}``` ')





client.run('what')

