from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

person = {"bob" : "good day to you!"}

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify('Hello!', 200)


@app.route('/goodbye', methods=['GET'])
def say_goodbye():
    return 'Goodbye!'

@app.route('/<username>')
def username(username):
    return "This is the username: " + username

# @app.route('/', methods = ['GET', 'POST'])
# def comment():
#     if request.method == 'POST':

@app.route('/user', methods = ['POST'])
def user():
    if request.is_json:
        user = request.get_json()
        print(user['username'])
        return jsonify("You always gotta return something!", 200)
    else:
        return jsonify("No payload was sent!", 400)
    

# POST -> /user := {user: coment}

if __name__ == '__main__':
    app.run(debug=True)
