import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import VideoFileClip
import datetime
from dotenv import load_dotenv

load_dotenv()
bot = os.getenv('tg_token')

# создание директории для временных файлов, если ее нет.
TEMP_PATH = 'temp/'
os.makedirs(TEMP_PATH, exist_ok=True)

# Функция для обработки фотографий и добавления водяного знака.
def process_photo(photo_file):
    # Загрузка фотографии.
    photo = Image.open(photo_file)

    # Добавление водяного знака.
    draw = ImageDraw.Draw(photo)
    font = ImageFont.load_default()
    watermark_text = "@melisad_sosedi"
    text_width, text_height = draw.textsize(watermark_text, font)
    watermark_position = (photo.width - text_width, photo.height - text_height)
    draw.text(watermark_position, watermark_text, fill=(255, 255, 255, 64), font=font)

    # Сохранение обработанной фотографии.
    processed_file = TEMP_PATH + 'processed_photo.jpg'
    photo.save(processed_file)
    return processed_file

# Функция для обработки видео и добавления водяного знака.
def process_video(video_file):
    # Загрузка видео.
    video = VideoFileClip(video_file)

    # Добавление водяного знака.
    watermark_text = "@melisad_sosedi"
    watermarked_video = video.set_duration(video.duration)
    watermarked_video = watermarked_video.set_position(("right", "bottom")).set_duration(video.duration)
    watermarked_video = watermarked_video.set_caption(watermark_text)

    # Сохранение обработанного видео.
    processed_file = TEMP_PATH + 'processed_video.mp4'
    watermarked_video.write_videofile(processed_file, codec="libx264")
    return processed_file
