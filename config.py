import typing as t

COMMAND_PREFIX = "$"

# Cogs in use
ACTIVE_COGS = [
    "cogs.stats",
    "cogs.tasks",
    "cogs.pin",
    "cogs.events",
    "cogs.info",
    "cogs.fun"  
]

# Server ID of server reaver-bot is residing in
PRIMARY_SERVER = int(915060648629665792)

# Hard Coded Channels used for server stats (user-friendly-name, prefix, channel-ID)
STATS_CHANNELS = [
    ("Playing Reaver", "🔴REAVING: {}", int(965597209657749515)),
    ("Online", "⭕RESTING: {}", int(965618451869732895)),
    ("Members", "⚫REAVERS: {}", int(965897679693545472))
] #type: t.List[t.Tuple[str, str, int]]

# Hard Coded Roles (user-friendly-name, role ID)
SERVER_ROLES = [
    ("Playing Reaver", int(965941196134432808))
] #type: t.List[t.Tuple[str, int]]

# Hard Coded Links (user-friendly-name, link)
SERVER_LINKS = [
    ("Steam", "https://store.steampowered.com/app/1890950/REAVER/"),
    ("Itch", "https://crunkz.itch.io/reaver"),
    ("Twitter", "https://twitter.com/crunkzah"),
    ("Youtube", "https://www.youtube.com/user/ddevit016ru"),
    ("Reddit", "https://www.reddit.com/r/reaver/"),
    ("Wiki", "https://reavergame.fandom.com/wiki/Reaver_Wiki"),
    ("Speedruns", "https://www.speedrun.com/reaver")
]

RSS_FEED = "https://steamcommunity.com/games/1890950/rss"