from flask import Flask, url_for

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def planet_choice(nickname, level, rating):
    html_content = f'''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                  integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                  crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
        </head>
        <body>
            <div>
                <h1 class="result">Результаты отборa</h1>
                <p class="results">Претендента на участие в миссии {nickname}:</p>
                <div class="alert alert-success" role="alert" id="phrase1" style="font-weight: 500">
                    Поздравляем! Ваш рейтинг после {level} этапа отбора
                </div>
                <h2 class="results">составляет {rating}!</h2>
                <div class="alert alert-warning" role="alert" id="phrase2" style="font-weight: 500">
                    Желаем удачи!
                </div>
            </div>
        </body>
        </html>
    '''
    return html_content


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
