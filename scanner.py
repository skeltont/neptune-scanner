import asyncio
from dis import disco
import requests
from dotenv import dotenv_values
import json
import discord
import pendulum

from models import Scan, Player

config = dotenv_values(".env")

class Client(discord.Client):
  async def setup_hook(self):
      self.loop.create_task(threat_scanning())

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)


def test_data():
  data = None

  with open('test_data.json') as f:
    data = json.load(f)

  return data


def galaxy_data():
  response = requests.post(
      "https://np.ironhelmet.com/api", params={
      "game_number": config['GAME_NUMBER'],
      "code": config["API_KEY"],
      "api_version": "0.1"
    }
  )

  return response.json()


def get_next_tick():
  now = pendulum.now()
  next_tick = now.add(hours=1)\
      .set(minute=int(config['TICK_RESET_MINUTE']))\
      .set(second=0)

  return (next_tick, now.diff(next_tick).in_seconds())


async def message_owner(message):
  user = await client.fetch_user(int(config['DISCORD_USER_ID']))
  await user.send(message)


async def threat_scanning():
  while True:
    data = galaxy_data()
    scan = Scan.build_from_scan_data(data['scanning_data'])
    owner = scan.player_by_alias(config["PLAYER_NAME"])

    scan_result = scan.threat_scan(owner)
    if scan_result is not None:
      await message_owner(scan_result)

    next_scan, sleep_duration = get_next_tick()
    print(f"Scan complete, next at: {next_scan.format('HH: mm: ss')}")
    await asyncio.sleep(sleep_duration)


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content == 'progress':
    await progress_scan(message.channel)
  elif message.content == 'technology':
    await technology_scan(message.channel)
  else:
    await message.channel.send('command not recognized. options: "progress" or "technology"')


async def technology_scan(channel):
  data = galaxy_data()
  scan = Scan.build_from_scan_data(data['scanning_data'])

  EMBED_MESSAGE_WRAPPER = "```{header}\n{rows}```"
  embed = discord.Embed(
      title="Technology Scans",
      description=EMBED_MESSAGE_WRAPPER.format(
          header="\t".join([
            Player.format_table_cell(h, 5)
            for h in Player.technology_display_headers()
          ]),
          rows="\n".join([p.technology_display()
                          for p in scan.players_by_total_tech()])
      )
  )

  await channel.send(content="Latest report on player technology", embed=embed)


async def progress_scan(channel):
  data = galaxy_data()
  scan = Scan.build_from_scan_data(data['scanning_data'])

  EMBED_MESSAGE_WRAPPER = "```{header}\n{rows}```"
  embed = discord.Embed(
      title="Progress Scans",
      description=EMBED_MESSAGE_WRAPPER.format(
          header="\t".join([
            Player.format_table_cell(h, 5)
            for h in Player.progress_display_headers()
          ]),
          rows="\n".join([p.progress_display()
                          for p in scan.players_by_strength()])
      )
  )

  await channel.send(content="Latest report on player strength", embed=embed)


client.run(config["DISCORD_TOKEN"])
