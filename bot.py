from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
updater = Updater(token='6566168833:AAH0-XJsQvBw4rDFHN-6yuIrUnvLbVyd2FM', use_context=True)
dispatcher = updater.dispatcher

def delete_file(update, context):
    file_id = update.message.document.file_id
    file_info = context.bot.get_file(file_id)
    file_path = file_info.file_path
    file_size = file_info.file_size

    # Check if there are any other files with the same size and name
    files_with_same_name = [f for f in os.listdir() if os.path.isfile(f) and os.path.getsize(f) == file_size and f == file_path]
    
    if len(files_with_same_name) > 1:
        # Delete the file
        os.remove(file_path)
        update.message.reply_text("File deleted successfully!")
    else:
        update.message.reply_text("There are no other files with the same size and name.")

delete_handler = MessageHandler(Filters.document, delete_file)
dispatcher.add_handler(delete_handler)

updater.start_polling()
updater.idle()
