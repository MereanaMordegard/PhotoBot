import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip
import datetime
from dotenv import load_dotenv

load_dotenv()
bot = os.getenv('tg_token')