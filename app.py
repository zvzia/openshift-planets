from datetime import datetime
from flask import render_template
import os


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here

    planety = ['merkury', 'wenus', 'ziemia', 'mars', 'jowisz', 'saturn', 'uran']

    dzisiaj = datetime.today()
    dzisiejsza_data = dzisiaj.strftime('%d.%m.%Y')
    dzien_tygodnia = dzisiaj.weekday()

    nazwa_planety = planety[dzien_tygodnia]

    return render_template('index.html',
                           dzisiejsza_data=dzisiejsza_data,
                           nazwa_planety=nazwa_planety)


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port, host='0.0.0.0')
