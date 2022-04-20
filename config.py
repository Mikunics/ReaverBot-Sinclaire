import typing as t

COMMAND_PREFIX = "$"

# Cogs in use
ACTIVE_COGS = [
    "cogs.stats",
    "cogs.tasks",
    "cogs.pin",
    "cogs.events"  
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