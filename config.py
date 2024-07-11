
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6786726247:AAE9OW_VPFBsf3q1pZ9RW8bbexsNySTGAnQ")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "21145186"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "daa53f4216112ad22b8a8f6299936a46")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQFCpmIAckiSX_7K8sL0X8LzEkP_7DYmk_mSC9p7EEo9auHBKG3EpOs5vsuwwa_h2gY-wv80FT12hzxa9xzpmPCKogXzTsQdy6THzUOVD_4gzXEiZJXWkvjt32KAhCJGMVfxj8sboRB_XSftdeRWTT7OqGyx83rr6I8uCLQv-PoREVWkWoK_uTyeYE7hTOHGNB4kb8df3LS2hhv0hqVCbaM0jXsk9n9lKMnHP677gcDQwftTCu5C9ZQcB1WHRdWfWh2hjXGKIfXTGM8-qlq8vbjIWECzOXorfjKw3v1nA3iWz8sHZDYWeTfk6CZvEQ9wWXAygL4-miGUDJzms6V1MRrQ2W8hPwAAAAGUhTlnAQ")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1002148186467w")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
