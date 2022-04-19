COMMAND_PREFIX = "$"

# Cogs in use
ACTIVE_COGS = [
    "cogs.stats",
    "cogs.tasks",
    "cogs.pin",
    "cogs.events"  
]

# Hard Coded Channels used for server stats (user-friendly-name, prefix, channel-ID, server-ID)
STATS_CHANNELS = [
    ("Playing Reaver", "🔴REAVING: {}", int(965597209657749515), int(915060648629665792)),
    ("Online", "⭕RESTING: {}", int(965618451869732895), int(915060648629665792)),
    ("Members", "⚫REAVERS: {}", int(965897679693545472), int(915060648629665792))
]

# Hard Coded Roles (user-friendly-name, role ID, server-ID)
SERVER_ROLES = [
    ("Playing Reaver", int(965941196134432808), int(915060648629665792))
]