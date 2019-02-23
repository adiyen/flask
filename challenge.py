from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

persons = {
    "krishna": "hello",
    "bob" : "good day to you!"
}

@app.route('/api/v1/user', methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET':
        arr = []
        for key, val in persons.items():
            arr.append(key + ": " + val)
        return jsonify(arr, 200)

    if request.method == 'POST':
        user = request.get_json()
        username = user.get("username")
        comment = user.get("comment")
        if username not in persons:
            persons[username] = comment
            return jsonify(comment, 200)
        else:
            return jsonify(400)

@app.route('/api/v1/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def spec_user(username):
    if request.method == 'GET':
        if username in persons:
            return jsonify(persons[username])

        else:
            return jsonify(400)

    if request.method == 'PUT':
        if username in persons:
            user = request.get_json()
            comment = user.get("comment")
            persons[username] = comment
            return jsonify(comment, 200)
        else:
            return jsonify(400)

    if request.method == 'DELETE':
        if username in persons:
            persons.pop(username)
            return jsonify(200)

        else:
            return jsonify(400)

if __name__ == '__main__':
    app.run(port = '1600', debug=True)  