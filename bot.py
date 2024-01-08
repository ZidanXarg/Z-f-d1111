import logging
from telegram import Bot, InputFile
from telegram.ext import Updater, CommandHandler

# Configure your bot token and channel IDs here
BOT_TOKEN = '6426959941:AAFn8NA_y6ySmnMRyt4Z3p2kvlqQdV7ILMY'
CHANNEL_1_ID = '-1001936730771'
CHANNEL_2_ID = '-1001941706320'

# Enable logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Initialize the bot and updater
bot = Bot(BOT_TOKEN)
updater = Updater(BOT_TOKEN)

# Define the function to start (send) and delete files
def start_and_delete_files(bot, update):
    try:
        # Get the name provided as a command argument
        name = update.message.text.split(' ', 1)[1]

        # Get all messages from the first channel
        messages = bot.get_chat_history(chat_id=CHANNEL_1_ID, limit=1000)

        for message in messages:
            if message.document and message.document.file_name == name:
                # Start (send) the file to the second channel
                bot.send_document(chat_id=CHANNEL_2_ID, document=InputFile(message.document.file_id))

                # Delete the forwarded file from the first channel
                bot.delete_message(chat_id=CHANNEL_1_ID, message_id=message.message_id)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Define the command handler for the start_and_delete_files command
updater.dispatcher.add_handler(CommandHandler('start_and_delete_files', start_and_delete_files))

# Start the bot
updater.start_polling()
