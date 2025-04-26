# from flask import Flask, render_template, request, jsonify
# import random
#
# app = Flask(__name__)
#
# # Инициализация игры (при каждом запуске сервера)
# число = random.randint(1, 100)
# попытки = 7
# сообщение = "Я загадал число от 1 до 100."
#
# @app.route('/')
# def index():
#     return render_template('index.html', сообщение=сообщение, попытки=попытки)
#
# @app.route('/guess', methods=['POST'])
# def guess():
#     global число, попытки, сообщение  # Добавлено global
#     try:
#         предположение = int(request.form['guess'])
#     except ValueError:
#         сообщение = "Пожалуйста, введите целое число."
#         return render_template('index.html', сообщение=сообщение, попытки=попытки)
#
#     попытки -= 1
#
#     if предположение < число:
#         сообщение = "Загаданное число больше."
#     elif предположение > число:
#         сообщение = "Загаданное число меньше."
#     else:
#         сообщение = f"Поздравляем! Вы угадали число {число} за {7 - попытки} попыток."
#         попытки = 0  # Заканчиваем игру
#     if попытки == 0 and сообщение != f"Поздравляем! Вы угадали число {число} за {7 - попытки} попыток.":
#       сообщение = f"Вы проиграли! Я загадал число {число}."
#
#     return render_template('index.html', сообщение=сообщение, попытки=попытки)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

# Глобальные переменные для состояния игры (плохой способ для продакшена, но для примера норм)
слово = ""
отгаданные_буквы = []
попытки = 6

@app.route("/", methods=['GET', 'POST'])
def index():
    global слово, отгаданные_буквы, попытки
    if request.method == 'POST':
        попытка = request.form['попытка'].lower()
        #TODO:  Добавить логику игры (обновление состояния, проверку победы/поражения)
        #      и передавать необходимые данные в шаблон.

    return render_template('index.html', display_word=отобразить_слово(слово, отгаданные_буквы), attempts_left=попытки)

if __name__ == "__main__":
    слово = выбрать_слово()
    app.run(debug=True) # !!! НЕ ИСПОЛЬЗУЙТЕ debug=True на продакшн сервере