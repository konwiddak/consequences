from flask import Flask, render_template, request, Markup
from dbs import get_users

app = Flask(__name__)

@app.route("/")
def new_game():
    return render_template('new_game.html')

@app.route('/join_game', methods=['POST'])
def create():
    data = request.form
    user = data['uname']
    gid = data['gid']
    #add user(data.uname)
    users = get_users(gid)
    users.append(user)
    us = "<br>\n".join(users)
    us = Markup(us)
    return render_template('lobby.html', users=us)

@app.route('/game', methods=['POST'])
def game():
    return render_template('draw.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
