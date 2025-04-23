import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "7115175533:AAHcFYSUzqagDMuxOttx4jLUNCDdlVyvtZo"
SUPPORT_USERNAME = "blackdjdj"
SOLANA_ADDRESS = "DVaoLjuk8qsc3KbM84JoCHNSFLuVpwtLsD6ac6jWuzWx"

bot = telebot.TeleBot(BOT_TOKEN)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🛒 Voir les services"))
menu.add(KeyboardButton("💬 Contacter le support"))

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Bienvenue sur BLACKDJLOG 🔥\nBoutique officielle. Choisis une option :", reply_markup=menu)

@bot.message_handler(func=lambda m: "services" in m.text.lower())
def services(message):
    txt = (
        "<b>🛍️ Services disponibles :</b>\n\n"
        "🔹 Spam lien : 25€ / 1k\n"
        "🔹 Tek Pristelle (3 SIM remboursables) : 50€\n"
        "🔹 Logs (FB, Amazon, Netflix, Mobiax) : 10€\n"
        "🔹 Comptes MEXT (crypto) : 50€\n"
        "🔹 Maillist : 5€/k\n"
        "🔹 Numlist ciblé : 5€/k\n\n"
        f"<b>💸 Paiement Solana :</b> <code>{SOLANA_ADDRESS}</code>\n"
        f"<b>📩 Support :</b> @{SUPPORT_USERNAME}"
    )
    bot.send_message(message.chat.id, txt, parse_mode="HTML")

@bot.message_handler(func=lambda m: "support" in m.text.lower())
def support(message):
    btn = InlineKeyboardMarkup()
    btn.add(InlineKeyboardButton("Contacter le support", url=f"https://t.me/{SUPPORT_USERNAME}"))
    bot.send_message(message.chat.id, "Clique ici pour le support :", reply_markup=btn)

@bot.message_handler(func=lambda m: True)
def fallback(message):
    bot.send_message(message.chat.id, "Commande inconnue. Utilise le menu ci-dessous.", reply_markup=menu)

bot.infinity_polling()
