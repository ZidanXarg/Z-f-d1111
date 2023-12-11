from config import *

from pyrogram import Client ,filters , enums
from pyrogram.errors import *
from time import sleep
import asyncio,re , random 

copier = Client (  "client someones account",
                api_id = API_ID,
                api_hash = API_HASH ,
                session_string = SESSION 
                ) 


def rsleep():
    return random.randint(1,30)
    
    
@copier.on_message(filters.private  & filters.command(['start'],['!','.']))
async def start(_, m):
    await m.delete()
    usr_name = m.from_user.first_name
    await m.reply(f"**you are {usr_name} , so What**")
    
    
@copier.on_message(filters.private & filters.command(['kang'],['!','.']))
async def kanger(c,m):
    await m.reply_chat_action(enums.ChatAction.TYPING)
    await m.reply('ok, go and enjoy your meal i will tell you when i am done🥰')
    for i in range(int(START),int( END)):
        #sleeps randomly to bypass telegram userbot detection
        rsl = rsleep()
        await asyncio.sleep(int(rsl))
        try:
            #not to forward such content, mean filter
            a = await copier.get_messages(FROM , int(i))
            #it jumps if the content is text 
            if a.text:
                pass
            # else a.document or a.video or a.audio or a.voice:
            else:
                await copier.copy_message(TO,from_chat_id=FROM, message_id=a.id)
        except Exception as e:
            pass
    await m.reply('i am Done')
  
    
@copier.on_message(filters.private & filters.command(['custom'],['!','.']))
async def kanger(c,m):
    #format from , to , start , end
    try :
        _ , CFROM ,CTO , CSTART , CEND = m.text.split(',')
    except :
        await m.reply("pls use this format   ```\n.custom , from , to , start , end \nexample\n\n .custom , -1001422072721 , -1002043404965 , 61546 , 63108```")
        return 
    await m.reply_chat_action(enums.ChatAction.TYPING)
    await m.reply('go and enjoy your meal i will tell you when i am done🥰')
    for i in range(int(CSTART), int(CEND)):
        rsl = rsleep()
        await asyncio.sleep(int(rsl))
        try:
            #not to forward such content, mean filter
            a = await copier.get_messages(int(CFROM) , int(i))
            #it jumps if the content is text 
            if a.text:
                pass
            # else a.document or a.video or a.audio or a.voice:
            else:
                await copier.copy_message(int(CTO),from_chat_id=int(CFROM), message_id=a.id)
        except Exception as e:
            pass
    await m.reply('i am Done')
	
print('running')
copier.run()
        
    
