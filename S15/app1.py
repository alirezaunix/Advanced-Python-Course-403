from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

CHOOSING_TYPE, ENTERING_AMOUNT, ENTERING_CAUSE = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [['رزرو ', 'کنسل']]
    
    await update.message.reply_text(
        'درود بر کله پوک ها',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    print(CHOOSING_TYPE)
    return CHOOSING_TYPE

def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    update.message.reply_text('Operation cancelled.')
    return ConversationHandler.END


async def f1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('chete.')
    print("test1")

def f2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("test2")
    
def main():
    token = "8382761518:AAGg9AH6aRibSpYEdFAFJYY1RTTmj23s7nA"
    application = Application.builder().token(token).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING_TYPE: [
                MessageHandler(filters.Regex('^(Income|Expense|Show Transactions)$'), 0)
            ],
            ENTERING_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, 0)],
            ENTERING_CAUSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, 0)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    application.add_handler(conv_handler)

    
    application.add_handler(CommandHandler("summary", f1))
    application.add_handler(CommandHandler("showTrans", f2))
    
    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()