from flask import Flask, request, render_template


def update_page():
    new_answer = ''
    know = ''
    try:
        if request.form['explain']:
            new_answer = str(request.form['explain'])
        else:
            know = str(request.form['know'])
    except ValueError:
        return render_template('index.html', error=1)
    if know == 'know':
        return know
    else:
        return new_answer

