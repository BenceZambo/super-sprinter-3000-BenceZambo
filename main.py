from flask import Flask, render_template
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def list_html():
    if request.method == 'GET':
        with open('datas.csv', "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(";") for element in lines]
    return render_template('list.html', datas=table)


"""@app.route('/story/<story_id>')
def form_id(story_id):
    return render_template()"""


@app.route('/story', methods=['POST'])
def form():
    id_of_story = 0
    if request.method == 'POST':
        id_of_story += 1
        title = request.form('title')
        user_story = request.form('user_story')
        criteria = request.form('criteria')
        business = request.form('business')
        time = request.form('time')
        status = request.form('status')
        with open('datas.csv', "a") as file:
            file.write(str(id_of_story))
            file.write(title)
            file.write(user_story)
            file.write(criteria)
            file.write(business)
            file.write(time)
            file.write(status)
            for record in table:
                row = ';'.join(record)
                file.write(row + "\n")
    return render_template('form.html')


if __name__ == '__main__':
    app.run()
