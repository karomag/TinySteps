import json

from flask import Flask, render_template, abort, request
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TelField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config.from_object('config')

with open('data/teachers.json') as f:
    teachers: list = json.load(f)
with open('data/goals.json') as f:
    goals: dict = json.load(f)


class BookingForm(FlaskForm):
    clientName = StringField('Вас зовут', [InputRequired()])
    clientPhone = TelField('Ваш телефон', [InputRequired()])
    clientWeekday = HiddenField()
    clientTime = HiddenField()
    clientTeacher = HiddenField()


@app.route('/')
@app.route('/index.html/')
def index():
    return 'Главная'


@app.route('/all/')
def all_page():
    return 'преподаватели'


@app.route('/goals/<string:goal>/')
def goal_page(goal):
    return f'цель {goal}'


@app.route('/profiles/<int:teacher_id>/')
def teacher_page(teacher_id=None):
    if teacher_id > len(teachers) - 1:
        abort(404)
    teacher: dict = teachers[teacher_id]
    goal: str = goals.get(teacher.get('goals')[0])
    title = f'Профиль {teacher["name"]}'
    return render_template('profile.html', title=title, teacher=teacher, goal=goal)


@app.route('/request/')
def request_form():
    return 'заявка на подбор'


@app.route('/request_done/')
def request_done():
    return 'заявка на подбор отправлена'


@app.route('/booking/<int:teacher_id>/<string:day>/<string:time>/')
def booking_form(teacher_id=None, day=None, time=None):
    form = BookingForm(clientWeekday=day, clientTime=time, clientTeacher=teachers[teacher_id])
    title = 'Заявка на урок'
    return render_template('booking.html', title=title, form=form)


@app.route('/booking_done/', methods=["POST"])
def booking_done():
    form = BookingForm()

    with open('data/booking.json') as f:
        booking_list = json.load(f)
    booking_list.append(request.form.to_dict())
    with open('data/booking.json', 'w') as f:
        json.dump(booking_list, f, indent=4, ensure_ascii=False)

    return render_template('booking_done.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
