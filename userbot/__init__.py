import os
import sys
import platform
from pyrogram import Client, enums

BOT_NAME    = "iSeven"
APP_VERSION = f"{BOT_NAME} 0.0.5"
DEV_MODEL   = "BraiFuck"

script_path = os.path.dirname(os.path.realpath(__file__))
if script_path != os.getcwd():
    os.chdir(script_path)

def die(msg):
    print(f"{msg} must be provided!", file=sys.stderr)
    sys.exit(1)

API_ID = os.getenv("24679387")
if API_ID is None:
    die("24679387")

API_HASH = os.getenv("ad9e119acbfc9de527e1da32fae2a866")
if API_HASH is None:
    die("ad9e119acbfc9de527e1da32fae2a866")

DATA_DIR = os.getenv("62895331328871")
if DATA_DIR is None:
    die("62895331328871")

SESSION_STRING = os.getenv("BQF4k9sAD3KzYaoYEKLz_v2OZ-0AmdoRY6ioKRFF4_QP46RRVQIG2Y_yuEmqWx5r7M7TERP1t5awTBCv0Jk7UQXlrAqEeLYAU_nVBiSjxKw3fUVWFdIgVNQpv2PKe1NXbV82FICNGG7d_FwE0IRgDNp-e4n3yjOL5D_Ye1ksnLvTCn2dCJ5HK0O1krOsmt0mRnfv1TCCqNk18VnAnyXSJrK5S8o9a0DoIu6AzL9L0yVQym5t4mL1aNbUthfXAmpA2Bxm10CHMrmdC5iGpNr5ZBAYcqUTtRiyOdKvwsNWPcszh_vU2AHx8hUXQ67Hzbr174BBn6aPH60QOOsi2IpmYqtRzwgQJgAAAAFkS9WpAA")
if SESSION_STRING is None:
    die("BQF4k9sAD3KzYaoYEKLz_v2OZ-0AmdoRY6ioKRFF4_QP46RRVQIG2Y_yuEmqWx5r7M7TERP1t5awTBCv0Jk7UQXlrAqEeLYAU_nVBiSjxKw3fUVWFdIgVNQpv2PKe1NXbV82FICNGG7d_FwE0IRgDNp-e4n3yjOL5D_Ye1ksnLvTCn2dCJ5HK0O1krOsmt0mRnfv1TCCqNk18VnAnyXSJrK5S8o9a0DoIu6AzL9L0yVQym5t4mL1aNbUthfXAmpA2Bxm10CHMrmdC5iGpNr5ZBAYcqUTtRiyOdKvwsNWPcszh_vU2AHx8hUXQ67Hzbr174BBn6aPH60QOOsi2IpmYqtRzwgQJgAAAAFkS9WpAA")

DB_NAME = os.getenv("userbot.sqlite")
if DB_NAME is None:
    die("DB_NAME")

DB_URL = os.getenv("mongodb+srv://iSeven:iSeven123@cluster0.hmuzzak.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
if DB_URL is None:
    pass

DB_TYPE = os.getenv("sqlite3")
if DB_TYPE is None:
    die("DB_TYPE")

app = Client(name=BOT_NAME,
             api_id=API_ID,
             api_hash=API_HASH,
             app_version=APP_VERSION,
             device_model=DEV_MODEL,
             workdir=script_path,
             sleep_threshold=30,
             system_version=platform.version() + " + " + platform.machine(),
             session_string=SESSION_STRING,
             parse_mode=enums.ParseMode.MARKDOWN
             )
