import json

from flask import Flask, render_template, abort

app = Flask(__name__)

with open('teachers.json', 'r') as f:
    teachers: list = json.load(f)
with open('goals.json', 'r') as f:
    goals: dict = json.load(f)


@app.route('/')
@app.route('/index.html/')
def index():
    return 'Главная'


@app.route('/all/')
def all_page():
    return 'преподаватели'


@app.route('/goals/<goal>/')
def goal_page(goal):
    return f'цель {goal}'


@app.route('/profiles/<int:teacher_id>/')
def teacher_page(teacher_id=None):
    if teacher_id > len(teachers) - 1:
        abort(404)
    teacher: dict = teachers[teacher_id]
    goal = goals.get(teacher.get('goals')[0])
    title = f'Профиль {teacher["name"]}'
    return render_template('profile.html', title=title, teacher=teacher, goal=goal)


@app.route('/request/')
def request_page():
    return 'заявка на подбор'


@app.route('/request_done/')
def request_done_page():
    return 'заявка на подбор отправлена'


@app.route('/booking/<int:teacher_id>/<string:day>/<string:time>/')
def booking_page(teacher_id=None, day=None, time=None):
    return f'форма бронирования {teacher_id} на {day} {time}'


@app.route('/booking_done/')
def booking_done_page():
    return 'заявка отправлена'


if __name__ == '__main__':
    app.run(debug=True)
