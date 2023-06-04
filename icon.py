import os; import base64

token = os.getenv('TOKEN')

headers = {

	  "Authorization": f"Bot {token}"}

def get_id():
  guild_id = ctx.guild.id

def guild_icon(id=get_id, link="url"):

  encode_img = base64.b64encode(requests.get(link).content).decode()

  ok = {

        "icon": f"data:image/jpeg;base64, {encode_img}"

}

  try:


    requests.patch(f"https://discord.com/api/v9/guilds/{id}", headers=headers, json=ok)

  except:
    pass
    
