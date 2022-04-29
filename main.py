from telebot import TeleBot
import os

app = TeleBot(__name__)
admin_chat_id = 365253585


@app.route('/shutdown')
def example_command(message):
    chat_dest = message['chat']['id']
    if message['chat']['id'] == admin_chat_id:
        msg = "Computer shutdown now"
        app.send_message(chat_dest, msg)

        os.system('shutdown -s')
    else:
        msg = "Fuck you"
        app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = '5039062554:AAE4RJmQ10Yw1Ft-325mXvOR_c0mqStDta4'
    app.poll(debug=True)
