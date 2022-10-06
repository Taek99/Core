from flask import Flask, render_template, request, redirect, session
app =Flask(__name__)
app.secret_key = 'verysecretkey'


@app.route('/')
def default_route():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] +=1
    return render_template("index.html")


@app.route('/count', methods=['POST'])
def counter_route():
    if request.form["counter"] == 'add2':
        session['count'] += 1
    elif request.form["counter"] == 'reset':
        session.clear()
    return redirect('/')
#i tried using elif request.form["counter"] == 'reset': session['count'] = 0 which didnt work not sure why make sure to ask later**************


@app.route('/destroy_session')
def destroy_route():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
