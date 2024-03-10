from flask import Flask, request, jsonify

app = Flask(__name__)

__persons = {}


@app.route('/persons/', methods=['GET'])
def get_persons():
    return jsonify(list(__persons.values())), 200  # OK


@app.route('/persons/<person_id>', methods=['GET'])
def get_person_by_id(person_id):
    person = __persons.get(int(person_id))
    if person:
        return jsonify(person), 200  # OK
    return jsonify(), 404  # Not Found


@app.route('/persons/', methods=['POST'])
def add_person():
    person = request.get_json()
    next_id = max(__persons.keys()) + 1 if __persons else 1
    person['pid'] = next_id
    __persons[next_id] = person
    return jsonify(), 201, {'Location': request.url + '/' + str(next_id)}  # Created


@app.route('/persons/<person_id>', methods=['DELETE'])
def delete_person_by_id(person_id):
    person_id = int(person_id)
    if person_id in __persons.keys():
        __persons.pop(person_id)
        return jsonify(), 204  # No Content
    return jsonify(), 404  # Not Found


@app.route('/persons/', methods=['PUT'])
def update_person():
    person = request.json
    person_id = person['pid']
    if person_id in __persons.keys():
        __persons[person_id] = person
        return jsonify(), 204  # No Content
    return jsonify(), 304  # Not Modified


if __name__ == '__main__':
    app.run()
