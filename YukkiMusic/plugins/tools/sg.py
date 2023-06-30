import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from YukkiMusic import userbot as us, app

ubot = us.one or us.two or us.three or us.four or us.five


@app.on_message(filters.command("sg"))
async def sg(client: Client, message: Message):
    if len(message.text.split()) < 1 and not message.reply_to_message:
        return await message.reply("sg username/id/reply")
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1]
    lol = await message.reply("<code>Processing...</code>")
    if args:
        try:
            user = await client.get_users(f"{args}")
        except Exception:
            return await lol.edit("<code>Please specify a valid user!</code>")
    bo = ["sangmata_bot", "sangmata_beta_bot"]
    sg = random.choice(bo)
    try:
        a = await ubot.send_message(sg, f"{user.id}")
    except Exception as e:
        return await lol.edit(e)
    await asyncio.sleep(1)
    async for stalk in ubot.get_chat_history(a.chat.id, 10):
        if not stalk:
            await message.reply("botnya ngambek")
        elif stalk:
            await message.reply(stalk.text)
    user_info = await ubot.resolve_peer(sg)
    await ubot.send(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    await lol.delete()
