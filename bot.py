import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8830057370:AAHVtGLv88oklq6ePuFyJCMtSH7_2gyG1yc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    welcome_text = (
        f"أهلاً بك يا {user.first_name}، أنا بوت **مفهي**! 🤖\n\n"
        "حارس مجموعتك... ومسلي أعضائك! 💎\n"
        "الأوامر المتاحة:\n"
        "• /start - لعرض هذه الرسالة\n"
        "• /help - المساعدة\n"
        "• /ping - فحص سرعة البوت"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = "🛠 **قائمة المساعدة:**\n\nأنا بوت «مفهي»، أساعدك في إدارة مجموعاتك وتسلية الأعضاء."
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("ابشرك يا سيمو، «مفهي» شغال وسريع بالسحابة 🚀!")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", ping))

    print("Bot 'Mofhi' is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()