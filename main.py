import telebot

TOKEN = "Ваш Telegram API Token"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(m):
    # Если бот не является администратором, то он не сможет удалить сообщение.
    try:
        bot.delete_message(m.chat.id,m.message_id)
    except:
        if m.new_chat_member.id != bot.get_me().id:
            bot.send_message(m.chat.id,"Пожалуйста, сделайте меня администратором, чтобы я мог удалить присоединение и оставлять сообщения в этой группе!")
        else:
            bot.send_message(m.chat.id,"Привет! Я ваш верный бот "Имя вашего бота" Спасибо что добавили меня! Чтобы использовать меня, сделайте меня администратором, и я смогу удалить все надоедливые уведомления, когда участник присоединяется к группе или покидает ее!")
        
@bot.message_handler(content_types=['left_chat_member'])
def delete_leave_message(m):
    # Если бот удаляется, он не сможет удалить сообщение о выходе.
    if m.left_chat_member.id != bot.get_me().id:
        try:
            bot.delete_message(m.chat.id,m.message_id)
        except:
            bot.send_message(m.chat.id,"Пожалуйста, сделайте меня администратором, чтобы я мог удалить присоединение и оставлять сообщения в этой группе!!")

bot.polling()