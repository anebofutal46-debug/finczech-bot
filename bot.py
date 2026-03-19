import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

TOKEN = "8616890992:AAGQs2lComaoUG7w7QMRPMFxr813_WhWqFs"

logging.basicConfig(level=logging.INFO)

# ==================== /start ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("💰 Kolik mohu získat?", callback_data="kolik"),
            InlineKeyboardButton("⚙️ Jak to funguje?", callback_data="jak"),
        ],
        [
            InlineKeyboardButton("⭐ Recenze klientů", callback_data="recenze"),
            InlineKeyboardButton("📩 Kontaktovat nás", callback_data="kontakt"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = (
        "👋 *Vítejte v FinCzech\\!*\n\n"
        "Každý rok tisíce lidí nechávají ležet peníze, na které mají nárok — jen proto, že o tom nevědí\\.\n\n"
        "*Vy to změnit můžete\\.*\n\n"
        "Za každý aktivní bankovní účet, který splňuje podmínky, získáváte *15 000 Kč\\.*\n\n"
        "✅ Bez poplatků\n"
        "✅ Bez rizika\n"
        "✅ Vše pod vaší kontrolou\n\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "Než začneme — rychlá otázka:\n"
        "*V kolika bankách máte aktivní účet nebo kartu?*\n\n"
        "_\\(Např\\. Raiffeisenbank, ČSOB, UniCredit, Moneta, Fio…\\)_"
    )

    await update.message.reply_text(text, parse_mode="MarkdownV2", reply_markup=reply_markup)


# ==================== /kolik ====================
async def kolik(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💰 *Kolik mohu získat?*\n\n"
        "Odměna je jednoduchá:\n\n"
        "🏦 1 účet \\= *15 000 Kč*\n"
        "🏦 2 účty \\= *30 000 Kč*\n"
        "🏦 3 účty \\= *45 000 Kč*\n\n"
        "Čím více účtů splňuje podmínky, tím více získáte\\.\n\n"
        "📊 Průměrný klient s námi získal *23 000 Kč\\.*\n\n"
        "Chcete zjistit, na kolik máte nárok?\n"
        "Napište nám přímo — zjistíme to společně\\! 👇"
    )
    await update.message.reply_text(text, parse_mode="MarkdownV2")


# ==================== /jak ====================
async def jak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⚙️ *Jak to funguje?*\n\n"
        "Proces je jednoduchý — trvá jen pár minut:\n\n"
        "*1️⃣ Napíšete nám* — ve kterých bankách máte účet\n"
        "*2️⃣ Odpovíte* na několik krátkých otázek\n"
        "*3️⃣ My připravíme* řešení přesně pro vás\n"
        "*4️⃣ Získáte odměnu* — 15 000 Kč za každý splňující účet\n\n"
        "💡 Nic neplatíte\\. Nic neriskujete\\.\n"
        "Vše probíhá transparentně a pod vaší kontrolou\\.\n\n"
        "Připraveni? Napište nám ve kterých bankách máte účet 👇"
    )
    await update.message.reply_text(text, parse_mode="MarkdownV2")


# ==================== /recenze ====================
async def recenze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "⭐ *Co říkají naši klienti*\n\n"
        "❝ _Nevěřila jsem tomu, ale dostala jsem 30 000 Kč za dva účty\\. Celé proběhlo rychle a bez problémů\\._ ❞\n"
        "— *Markéta, Praha*\n\n"
        "❝ _Skeptický jsem byl, ale vše bylo transparentní\\. Doporučuji každému\\._ ❞\n"
        "— *Tomáš, Brno*\n\n"
        "❝ _Za hodinu práce jsem získal 15 000 Kč\\. Proč jsem to neudělal dříve?_ ❞\n"
        "— *Pavel, Ostrava*\n\n"
        "❝ _Myslela jsem, že je to složité\\. Ale bylo to jednodušší než jsem čekala\\._ ❞\n"
        "— *Jana, Plzeň*\n\n"
        "📩 Chcete být další? Napište nám ve kterých bankách máte účet 👇"
    )
    await update.message.reply_text(text, parse_mode="MarkdownV2")


# ==================== /kontakt ====================
async def kontakt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📩 *Kontaktujte nás*\n\n"
        "Jsme tu pro vás — napište přímo do tohoto chatu\\.\n"
        "Odpovíme co nejdříve\\.\n\n"
        "🌐 Facebook: [FinCzech](https://www.facebook.com/profile.php?id=100094178872598)\n"
        "🏢 IČO: 242 73 821\n\n"
        "⏰ Pracujeme: Po–Ne, 9:00–21:00"
    )
    await update.message.reply_text(text, parse_mode="MarkdownV2", disable_web_page_preview=True)


# ==================== КНОПКИ ====================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "kolik":
        text = (
            "💰 *Kolik mohu získat?*\n\n"
            "Odměna je jednoduchá:\n\n"
            "🏦 1 účet \\= *15 000 Kč*\n"
            "🏦 2 účty \\= *30 000 Kč*\n"
            "🏦 3 účty \\= *45 000 Kč*\n\n"
            "Čím více účtů splňuje podmínky, tím více získáte\\.\n\n"
            "📊 Průměrný klient s námi získal *23 000 Kč\\.*\n\n"
            "Chcete zjistit, na kolik máte nárok?\n"
            "Napište nám přímo — zjistíme to společně\\! 👇"
        )
    elif query.data == "jak":
        text = (
            "⚙️ *Jak to funguje?*\n\n"
            "Proces je jednoduchý — trvá jen pár minut:\n\n"
            "*1️⃣ Napíšete nám* — ve kterých bankách máte účet\n"
            "*2️⃣ Odpovíte* na několik krátkých otázek\n"
            "*3️⃣ My připravíme* řešení přesně pro vás\n"
            "*4️⃣ Získáte odměnu* — 15 000 Kč za každý splňující účet\n\n"
            "💡 Nic neplatíte\\. Nic neriskujete\\.\n"
            "Vše probíhá transparentně a pod vaší kontrolou\\.\n\n"
            "Připraveni? Napište nám ve kterých bankách máte účet 👇"
        )
    elif query.data == "recenze":
        text = (
            "⭐ *Co říkají naši klienti*\n\n"
            "❝ _Nevěřila jsem tomu, ale dostala jsem 30 000 Kč za dva účty\\. Celé proběhlo rychle a bez problémů\\._ ❞\n"
            "— *Markéta, Praha*\n\n"
            "❝ _Skeptický jsem byl, ale vše bylo transparentní\\. Doporučuji každému\\._ ❞\n"
            "— *Tomáš, Brno*\n\n"
            "❝ _Za hodinu práce jsem získal 15 000 Kč\\. Proč jsem to neudělal dříve?_ ❞\n"
            "— *Pavel, Ostrava*\n\n"
            "❝ _Myslela jsem, že je to složité\\. Ale bylo to jednodušší než jsem čekala\\._ ❞\n"
            "— *Jana, Plzeň*\n\n"
            "📩 Chcete být další? Napište nám ve kterých bankách máte účet 👇"
        )
    elif query.data == "kontakt":
        text = (
            "📩 *Kontaktujte nás*\n\n"
            "Jsme tu pro vás — napište přímo do tohoto chatu\\.\n"
            "Odpovíme co nejdříve\\.\n\n"
            "🌐 Facebook: [FinCzech](https://www.facebook.com/profile.php?id=100094178872598)\n"
            "🏢 IČO: 242 73 821\n\n"
            "⏰ Pracujeme: Po–Ne, 9:00–21:00"
        )
    else:
        text = "Napište nám přímo do chatu 👇"

    await query.edit_message_text(text, parse_mode="MarkdownV2", disable_web_page_preview=True)


# ==================== ОБЫЧНЫЕ СООБЩЕНИЯ ====================
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✅ *Děkujeme za zprávu\\!*\n\n"
        "Náš specialista se s vámi spojí co nejdříve\\.\n\n"
        "⏰ Obvykle odpovídáme do 15 minut\\.\n"
        "Pracujeme: Po–Ne, 9:00–21:00"
    )
    await update.message.reply_text(text, parse_mode="MarkdownV2")


# ==================== ЗАПУСК ====================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("kolik", kolik))
    app.add_handler(CommandHandler("jak", jak))
    app.add_handler(CommandHandler("recenze", recenze))
    app.add_handler(CommandHandler("kontakt", kontakt))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot běží...")
    app.run_polling()


if __name__ == "__main__":
    main()
