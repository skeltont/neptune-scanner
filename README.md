# Neptune's Pride SentryScanner

collecting data on your foes and receiving early warning when your systems have a scanned
fleet on its way.

## Useful links
- [NP API Documentation](https://forum.ironhelmet.com/t/api-documentation-player-written/7533)
- [Adding a bot to discord](https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro)

## install
```
/usr/bin/python3.8 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## configuration
```
# .env
GAME_NUMBER= # your Neptune's Pride game number
API_KEY= # your Neptune's Pride API key
PLAYER_NAME= # your alias in the game so it can check ownership
TICK_RESET_MINUTE= # which minute of the hour do you want to scan for threats.
                   # recommended a few minutes after reset so there's no race
                   # condition with stale data from last tick.

DISCORD_USER_ID= # your discord user id since this is your data

DISCORD_TOKEN= # Discord bot secret token
```

## usage
```
python scanner.py
```

then you can use simple commands in by messaging bot directly in discord, like:
```
progress
technology
```
for this first implementation, I was lazy about how we message this bot. it's your
personal api key so this isn't meant for being added to a public server. The script
will use the discord client to message you directly every tick if there's an incoming threat
and you can simply reply with the two commands above to get some quick readouts on player
progression and technology.

Future work would be to properly integrate the discord-slash-commands like i initially wanted
to do, but since their api is for a single player this could honestly just be replaced with
some code that emails you. I just wanted to mess around with discord.py a bit and only
just found out that discord.py isn't being maintained anymore.

## notes
kept the test_data I was using, which is an example of the API response so you can test
without hitting their API server repeatedly.

## examples
**Progress Scan**

![example_progress_scan](https://user-images.githubusercontent.com/4512337/186812369-3bac7335-68ee-4377-98f7-914257c72f71.jpg)

**Technology Scan**

![example_tech_scan](https://user-images.githubusercontent.com/4512337/186812377-4a58ac9f-1e3a-417a-9517-575aae53843b.jpg)

