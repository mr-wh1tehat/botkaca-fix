# GOAL:
# load config

import os
from bot.config import Config

CONFIG = Config({
    'ROOT' : os.getcwd(),
    'WORKDIR' : 'sessions',
    'LOG_FILE' : 'log.txt',
    'MAX_LOG_SIZE' : 10 * 1024 * 1024,
    'API_HASH' : '28b864c5a410bb2ae9d0e16672b6e02d',
    'API_ID' : '576732',
    'BOT_TOKEN' : '5394915938:AAHzXY6H1VJ4zPyTwREKPftOoyNAzrUhEp8',
    'BOT_PASSWORD' : 0000,
    'CHAT_ID' : 'group id',
    'SUDO_USERS' : 5354345941,
    'EDIT_SLEEP' : 20,
    'UPLOAD_MAX_SIZE' : 2000 * 1024 * 1024,
    'UPLOAD_AS_DOC' : 0,
    'UPLOAD_AS_ZIP' : 0,
    'ARIA2_DIR' : 'downloads',
    'TORRENT_TRACKER' : '',
    'BAR_SIZE' : 10,
    'THUMBNAIL_NAME' : 'default_thumbnail.jpg',
    'LOCAL' : 'en'
})

# GOAL:
# prepare workdir

workdir = os.path.join(CONFIG.ROOT, CONFIG.WORKDIR)
if not os.path.isdir(workdir):
    os.mkdir(workdir)
del workdir

# GOAL:
# logging any important sign

logfile = os.path.join(CONFIG.ROOT, CONFIG.WORKDIR, CONFIG.LOG_FILE)

if os.path.exists(logfile):
    with open(logfile, "r+") as f_d:
        f_d.truncate(0)

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            logfile,
            maxBytes=CONFIG.MAX_LOG_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# GOAL:
# Log configuration

LOGGER.info(dict(CONFIG))

del logfile

# GOAL:
# Localization

LOCAL = __import__(name = 'bot.locals.' + CONFIG.LOCAL, fromlist = ['LOCAL']).LOCAL

# GOAL:
# load Command format

COMMAND = Config({
    'HELP' : 'help',
    'LEECH' : 'leech',
    'CANCEL_LEECH' : 'cancel',
    'LEECH_LIST' : 'status',
    'UPLOAD_AS_DOC' : 'upload_as_doc',
    'UPLOAD_AS_ZIP' : 'upload_as_zip',
    'SET_THUMBNAIL' : 'save',
    'RESET_THUMBNAIL' : 'clear',
    'SET_TRACKER' : 'set_tracker'
}, 'COMMAND_')

# GOAL:
# set status

STATUS = type('obj', (object,), {
    'ARIA2_API' : None,
    'UPLOAD_AS_DOC' : bool(int(CONFIG.UPLOAD_AS_DOC)),
    'UPLOAD_AS_ZIP' : bool(int(CONFIG.UPLOAD_AS_ZIP)),
    'DEFAULT_TRACKER' : CONFIG.TORRENT_TRACKER.split(','),
    'CHAT_ID' : CONFIG.CHAT_ID.split(',')
})
