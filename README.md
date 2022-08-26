# Neptune's Pride SentryScanner

collecting data on your foes

[API Documentation](https://forum.ironhelmet.com/t/api-documentation-player-written/7533)
[Adding a bot to discord](https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro)
[Discord interactions quickstart](https://discord-interactions.readthedocs.io/en/latest/quickstart.html)

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
DISCORD_TOKEN= # Discord bot secret token
DISCORD_GUILD_ID= # Discord server guild ID
```

## usage
```
python sentry-scanner.py
```

then you can use slash commands in discord, like:
```
/progress_scan
/technology_scan
```
for this first implementation

## notes
kept the test_data I was using, which is an example of the API response so you can test
without hitting their API server repeatedly.

## examples
**Progress Scan**

![example_progress_scan](https://user-images.githubusercontent.com/4512337/186812369-3bac7335-68ee-4377-98f7-914257c72f71.jpg)

**Technology Scan**

![example_tech_scan](https://user-images.githubusercontent.com/4512337/186812377-4a58ac9f-1e3a-417a-9517-575aae53843b.jpg)

