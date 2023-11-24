from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "postgres://mbriubpn:m2tWxb_RrtWOhqlFCCm000JEpLpAtZZo@tai.db.elephantsql.com/mbriubpn"]
        API_HASH = [str, "90da70b17365b3709b8a0346a7749ce7"]
        API_ID = [int, 20421248]
        BOT_TOKEN = [str, "6633234800:AAGOiWkNZg_E31Q9FZatrW979esrWP5GJ1A"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[5009250822]]
        OWNER_ID = [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"https://t.me/+VaTnv2H60IExZDY1"]
        FORCEJOIN_ID = [int,-1001863995845]

        TRACE_CHANNEL = [int, -1002001018139]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
