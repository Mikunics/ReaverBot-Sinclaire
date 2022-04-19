COMMAND_PREFIX = "$"

# Cogs in use
ACTIVE_COGS = [
    "cogs.stats",
    "cogs.tasks",
    "cogs.pin",
    "cogs.events"  
]

# Hard Coded Channels used for server stats (user-friendly-name, Prefix, channel-id, server-id)
STATS_CHANNELS = [
    ("Playing Reaver", "🔴REAVING: {}", 965597209657749515, 915060648629665792),
    ("Online", "⭕RESTING: {}", 965618451869732895, 915060648629665792),
    ("Members", "⚫REAVERS: {}", 965084897402306600, 915060648629665792)
]