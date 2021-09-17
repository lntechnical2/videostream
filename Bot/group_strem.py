import re 
import os
import time 
from pytgcalls import GroupCallFactory
from pyrogram import Client, filters
from pyrogram.types import Message
# from py_youtube import ytdl
from py_youtube import ytdl ,Data

from Bot.video_stream import app

group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)
VIDEO_CALL = {}



@Client.on_message(filters.group & filters.command(["stream"]))
async def play(client, m: Message):
	if (m.reply_to_message):
			time.sleep(3)
			get =await client.get_chat_member(m.chat.id,m.from_user.id)
			status = get. status
			cmd_user = ["administrator","creator"]
			if status in cmd_user:
				     link = m.reply_to_message.text
				     youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
				     youtube_regex_match = re.match(youtube_regex, link)
				     if youtube_regex_match:
				     	try:
				     	       data = Data(link).data()
				     	       video_url = ytdl(link).besturl()
				     	except Exception as e:
				     	       await m.reply(f"**Error** -- `{e}`")
				     	       return
				     	try:
				     		group_call = group_call_factory.get_group_call()
				     		await group_call.join(m.chat.id)
				     		await group_call.start_video(video_url,enable_experimental_lip_sync=True)
				     		VIDEO_CALL[m.chat.id] = group_call
				     		await client.send_photo(m.chat.id,photo=data["thumbnails"],caption =f"**Title :{data['title']}**\n**Views :{data['views']}**\n**Likes : {data['likes']}**",reply_to_message_id=m.message_id)
				     	
				     	except Exception as e:
				         	await m.reply(f"**Error** -- `{e}`")
				     else:
			         	try:
			         		group_call = group_call_factory.get_group_call()
			         		await group_call.join(m.chat.id)
			         		await group_call.start_video(link,enable_experimental_lip_sync=True)
			         		VIDEO_CALL[m.chat.id] = group_call
			         		await m.reply("** Started Streaming!**")
			         	except Exception as e:
			         	    	await m.reply(f"**Error** -- `{e}`")
				             	
					
			
				             	

@Client.on_message(filters.group & filters.command(["stopstream"]))
async def stop (client, m: Message):
	time.sleep(3)
	get =await client.get_chat_member(m.chat.id,m.from_user.id)
	status = get. status
	cmd_user = ["administrator","creator"]
	if status in cmd_user:
	       try:
	       	await VIDEO_CALL[m.chat.id].stop()
	       	await m.reply("** Stopped Streaming!**")
	       except Exception as e:
	       	await m.reply(f"**Error** - `{e}`")
