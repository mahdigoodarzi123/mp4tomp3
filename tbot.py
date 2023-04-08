
import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from mp4tomp3 import converter
import os

token = "YOUR TOKEN"
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
bot = telegram.Bot(token = token)

users = []  

def start(update: Update, context):
    update.message.reply_text('Hi! Send me a video and I will split its voices from it.(programmer: @erfan_owl121 )')

def download_video(update: Update, context):
    """Download the video that the user sent."""
    # Get the file ID of the video sent by the user
    file_id = update.message.video.file_id
    
    # Use the file ID to get the video file object
    video_file = context.bot.get_file(file_id)
    
    # Download the video file to the "downloads" directory
    video_file.download("video.mp4")
    
    # Send a confirmation message to the user
    update.message.reply_text('Video downloaded successfully!')

    # calling the converter function to convert the video
    converter("video.mp4")
    update.message.reply_text('the voice has been splitted from the video')

    # removing the video
    os.remove('video.mp4')

    # sending the voice
    chat_id = update.message.chat_id
    bot.sendAudio(chat_id=chat_id, audio=open('sound.mp3', 'rb'))
    os.remove("sound.mp3")
    users.append(chat_id)
    print(len(users))



def main():
    """Start the bot."""
    # Create the Updater and pass in your bot token
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))

    # Add message handlers
    dp.add_handler(MessageHandler(Filters.video, download_video))

    # Start the bot
    updater.start_polling()
    logger.info("Bot started.")

    # Run the bot until you press Ctrl-C or the process is stopped
    updater.idle()

if __name__ == '__main__':
    main()