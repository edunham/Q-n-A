from flask import Flask, render_template, request
from update import *
import os

## Global variables seem like the best way to do this I guess.
## Alternatively, we could store in a file.
answers = []
know = 0

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST', 'GET'])
def update():
    global answers
    global know
    new_answer = update_page()
    print new_answer
    if new_answer=="know":
        know += 1
    else: 
        answers.append(new_answer)
    total = know + len(answers)
    percent = (float(know)/total)*100
    return render_template('/chart.html', answers=answers, know=know, total=total, percent=percent) 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
