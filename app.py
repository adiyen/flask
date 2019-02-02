from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

persons = {
    "krishna": "hello",
    "bob" : "good day to you!"
}

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/user/<username>', methods=['GET'])
def username(username):
    if request.method == 'GET':
        if persons.get(username):
            return username + " " + persons[username]
        else:
            return "No comment!"

@app.route('/user', methods=['POST', 'PUT', 'DELETE'])
def new_user():
    if request.method == 'POST':
        user = request.get_json()
        username = user.get("username")
        comment = user.get("comment")
        if username not in persons:
            persons[username] = comment
            return jsonify(comment, 200)
        else:
            return jsonify(400)

    if request.method == 'PUT':
        user = request.get_json()
        username = user.get("username")
        comment = user.get("comment")
        if username in persons:
            persons[username] = comment
            return jsonify(comment, 200)
        else:
            return jsonify(400)

    if request.method == 'DELETE':
        user = request.get_json()
        username = user.get("username")
        if username in persons:
            persons.pop(username)
            return jsonify(persons, 200)
        else:
            return jsonify(400)

if __name__ == '__main__':
    app.run(debug=True)
