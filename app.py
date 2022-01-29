from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Главная'


@app.route('/all')
def all_page():
    return 'преподаватели'


@app.route('/goals/<goal>/')
def goal_page(goal):
    return f'цель {goal}'


@app.route('/profiles/<teacher_id>/')
def teacher_page(teacher_id):
    return f'преподаватель {teacher_id}'


@app.route('/request/')
def request_page():
    return 'заявка на подбор'


@app.route('/request_done/')
def request_done_page():
    return 'заявка на подбор отправлена'


@app.route('/booking/<teacher_id>/<day>/<time>/')
def booking_page(teacher_id, day, time):
    return f'форма бронирования {teacher_id} на {day} {time}'


@app.route('/booking_done/')
def booking_done_page():
    return 'заявка отправлена'


if __name__ == '__main__':
    app.run()
