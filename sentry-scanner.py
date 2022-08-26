import requests
from dotenv import dotenv_values
import json
import interactions

from models import Scan, Player

neptunes_pride_api_address = "https://np.ironhelmet.com/api"
config = dotenv_values(".env")
bot = interactions.Client(token=config["DISCORD_TOKEN"])

def test_data():
  data = None

  with open('test_data.json') as f:
    data = json.load(f)

  return data

def perform_scan():
  response = requests.post(
    neptunes_pride_api_address, params = {
      "game_number": config['GAME_NUMBER'],
      "code": config["API_KEY"],
      "api_version": "0.1"
    }
  )

  return response.json()


@bot.command(name="progress_scan", scope=config['DISCORD_GUILD_ID'])
async def progress_scan(ctx: interactions.CommandContext):
  data = perform_scan() # test_data()
  scan = Scan.build_from_scan_data(data['scanning_data'])

  EMBED_MESSAGE_WRAPPER = "```{header}\n{rows}```"
  embed = interactions.Embed(
    title="Progress Scans",
    description=EMBED_MESSAGE_WRAPPER.format(
      header="\t".join([
        Player.format_table_cell(h, 5)
        for h in Player.progress_display_headers()
      ]),
      rows="\n".join([p.progress_display() for p in scan.players_by_strength()])
    )
  )

  await ctx.send(content="Latest report on player strength", embeds=[embed])


@bot.command(name="technology_scan", scope=config['DISCORD_GUILD_ID'])
async def progress_scan(ctx: interactions.CommandContext):
  data = perform_scan() # test_data()
  scan = Scan.build_from_scan_data(data['scanning_data'])

  EMBED_MESSAGE_WRAPPER = "```{header}\n{rows}```"
  embed = interactions.Embed(
    title="Technology Scans",
    description=EMBED_MESSAGE_WRAPPER.format(
      header="\t".join([
        Player.format_table_cell(h, 4)
        for h in Player.technology_display_headers()
      ]),
      rows="\n".join([p.technology_display() for p in scan.players_by_total_tech()])
    )
  )

  await ctx.send(content="Latest report on player strength", embeds=[embed])

bot.start()



