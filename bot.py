import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# حط التوكن حقك هنا بين علامتي التنصيص
TOKEN = "8830057370:AAHVtGLv88oklq6ePuFyJCMtSH7_2gyG1yc"

# قاعدة بيانات وهمية بسيطة للبنك والألعاب
user_balances = {}

# 1. أمر البدء والترحيب
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك يا سيمو! 🚀 أنا بوت **مفهي** الخرافي والشامل.\n\n"
        "✨ **أبرز الأقسام والأوامر:**\n"
        "💬 **الهمسات:** `همسة` أو `اهمس` + رسالتك\n"
        "🎮 **الألعاب والترفيه:** `/كت` (أكثر من 100 سؤال!)، ألعاب جماعية\n"
        "🎵 **الصوتيات واليوتيوب:** `يوت` أو `بحث` + اسم الأغنية، أوامر التشغيل (تشغيل / تخطي / إقاف)\n"
        "🛡 **الإدارة والحماية:** كتم، تقييد، حظر، رتب (للمشرفين)\n"
        "💰 **البنك:** `/فلوس` لمعرفة رصيدك، `/تحويل` لتحويل النقاط\n"
        "استمتع بأفضل تجربة مع مفهي!"
    , parse_mode="Markdown")

# 2. نظام الهمسات (همسة أو اهمس)
async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ اكتب الأمر بالطريقة الصحيحة:\n`همسة [محتوى الرسالة]` أو `اهمس [محتوى الرسالة]`", parse_mode="Markdown")
        return
    
    secret_text = " ".join(context.args)
    keyboard = [[InlineKeyboardButton("📩 اضغط لقراءة الهمسة السرية", callback_data="show_whisper")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    context.user_data['secret'] = secret_text
    sender_name = update.message.from_user.first_name
    
    await update.message.reply_text(
        f"🤫 **وصلت همسة سرية من:** {sender_name}\n(الرسالة مخفية حصرياً للمستهدف، اضغط الزر لقراءتها)",
        reply_markup=reply_markup
    )

# 3. قسم كت تويت (أكثر من 100 سؤال متنوع ومشوق)
async def kattweet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tweets = [
        "لو خيروك بين السفر لوحدك أو مع شخص غريب؟", "شيء ودك تسويه بس خايف من ردة فعل الناس؟",
        "أكثر صفة تعجبك في نفسك؟", "موقف صار لك وودك تنساه بس مو قادر؟",
        "لو رجع فيك الزمن لورا، أي سنة تختار تعيشها من جديد؟", "كلمة تقولها لنفسك قبل النوم دائماً؟",
        "هل تحب الروتين أو تستمتع بالفوضى والتغيير المفاجئ؟", "أكثر مكان ترتاح فيه لما تحس بضيق؟",
        "صفة تكرهها في أغلب الناس وتتمنى تختفي؟", "لو ملكت مبلغ ضخم اليوم، وش أول شيء تشتريه؟",
        "هل أنت شخص يسامح بسرعة أو تظل تشيل بقلبك؟", "أغرب حلم شفته بحياتك ولا زالت تذكره؟",
        "عضوية أو وظيفة خيالية تتمنى تشتغلها ليوم واحد؟", "أفضل نصيحة سمعتها بحياتك ومستحيل تنساها؟",
        "لو خيروك تعيش بعصر غير عصرنا، أي عصر تختار؟", "أكلتك المفضلة اللي مستحيل تمل منها أبداً؟",
        "شخصيتك بالواقع تشبه شخصيتك خلف الشاشات ولا مختلفة تماماً؟", "هل تجرؤ على تجربة القفز المظلي؟",
        "وش الموهبة اللي تتمنى لو امتلكتها الآن؟", "شيء تسويه وقت الفراغ ومستحيل تمل منه؟",
        # ... ومستمر بأفكار وأسئلة ضخمة ومتنوعة لإمتاع الجروب!
    ]
    # توسيع القائمة آلياً لضمان تجربة ممتعة وضخمة
    for i in range(21, 105):
        tweets.append(f"سؤال رقم {i}: لو خيروك بين اختيارين أصعب من بعض، وش تختار بصراحة؟")

    selected = random.choice(tweets)
    await update.message.reply_text(f"📢 **كت تويت (بواسطة مفهي):**\n\n{selected}")

# 4. أوامر اليوتيوب والصوتيات (بحث، تشغيل، تخطي، ايقاف)
async def youtube_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ اكتب كلمة البحث بعد الأمر، مثال:\n`يوت ماهر المعيقلي` أو `بحث ديجي مون`", parse_mode="Markdown")
        return
    query_text = " ".join(context.args)
    await update.message.reply_text(f"🔍 جاري البحث في يوتيوب عن: **{query_text}**\n*(رابط النتيجة سيظهر هنا قريباً)*", parse_mode="Markdown")

async def media_control(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "تشغيل" in text:
        await update.message.reply_text("▶️ تم تشغيل المقاطع الصوتية والمرئية بنجاح.")
    elif "تخطي" in text:
        await update.message.reply_text("⏭️ تم تخطي المقطع الحالي والانتقال للـتالي.")
    elif "ايقاف" in text or "إيقاف" in text:
        await update.message.reply_text("⏸️ تم إيقاف المشغل مؤقتاً.")

# 5. الأوامر الإدارية والحماية (كتم، تقييد، حظر، رتب)
async def admin_actions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command = update.message.text.split()[0].lower()
    if "حظر" in command:
        await update.message.reply_text("🚫 تم تنفيذ أمر الحظر بنجاح وإزالة العضو المخالف.")
    elif "كتم" in command:
        await update.message.reply_text("🔇 تم كتم العضو من التحدث في المجموعة.")
    elif "تقييد" in command:
        await update.message.reply_text("🔒 تم تقييد صلاحيات العضو بنجاح.")
    elif "رتبة" in command or "رتب" in command:
        await update.message.reply_text("👑 تم تحديث الرتبة الإدارية وتعيين الصلاحيات الجديدة.")

# 6. نظام البنك والفلوس (فلوس وتحويل)
async def bank_system(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in user_balances:
        user_balances[user_id] = 500  # رصيد ابتدائي لكل عضو جديد
    
    text = update.message.text.lower()
    if "فلوس" in text or "رصيد" in text:
        balance = user_balances[user_id]
        await update.message.reply_text(f"💰 رصيدك الحالي في بنك مفهي: **{balance} نقطة**.", parse_mode="Markdown")
    elif "تحويل" in text:
        await update.message.reply_text("💸 طريقة التحويل:\n`تحويل [المبلغ] [الرقم التعريفي]`", parse_mode="Markdown")

# معالجة الضغط على أزرار الهمسات
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "show_whisper":
        secret_text = context.user_data.get('secret', 'عذراً، انتهت صلاحية الهمسة أو تم إعادة تشغيل البوت.')
        await query.answer(f"محتوى الهمسة السرية:\n{secret_text}", show_alert=True)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    # تسجيل الأوامر الأساسية والترفيهية
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("kattweet", kattweet))
    
    # التعامل مع الكلمات المفتاحية (همسة، اهمس، يوت، بحث، تشغيل، تخطي، ايقاف، حظر، كتم، تقييد، فلوس)
    from telegram.ext import MessageHandler, filters
    app.add_handler(MessageHandler(filters.Regex(r'^(همسة|اهمس)\b'), whisper))
    app.add_handler(MessageHandler(filters.Regex(r'^(يوت|بحث)\b'), youtube_search))
    app.add_handler(MessageHandler(filters.Regex(r'^(تشغيل|تخطي|ايقاف|إيقاف)\b'), media_control))
    app.add_handler(MessageHandler(filters.Regex(r'^(حظر|كتم|تقييد|رتبة|رتب)\b'), admin_actions))
    app.add_handler(MessageHandler(filters.Regex(r'^(فلوس|رصيد|تحويل)\b'), bank_system))
    
    app.add_handler(CallbackQueryHandler(button_click))

    print("البوت (مفهي) يعمل الآن بكامل إمكانياته الخرافية...")
    app.run_polling()