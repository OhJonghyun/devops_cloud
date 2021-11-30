import telegram

token = "2106416343:AAEbQFCF_ok5ZuG20HKOmCycEnqCpMj8qdg"
bot = telegram.Bot(token)
bot.sendMessage(chat_id="사용자아이디", text="안녕하세요. 저는 봇입니다.")
