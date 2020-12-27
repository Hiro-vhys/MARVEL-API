from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

with open('MarvelApi.json', 'r') as marvel_api:
    input_json = marvel_api.read()

input_dict = json.loads(input_json)


@app.route('/', methods=['GET'])
def defaultRoute():
    index = '<h1>Endpoints disponiveis</h1><br>'
    index += '<p>character_id 1, 2, 3, 4 or 5</p>'
    index += '<p>/v1/public/characters</p>'
    index += '<p>/v1/public/characters/character_id</p>'
    index += '<p>/v1/public/characters/character_id/comics</p>'
    index += '<p>/v1/public/characters/character_id/events</p>'
    index += '<p>/v1/public/characters/character_id/series</p>'
    index += '<p>/v1/public/characters/character_id/stories</p>'
    return index


def errorHandling(character_id):
    if character_id.isdecimal() and 0 < int(character_id) < 6:
        return True
    else:
        return False


def searchOnJson(character_id, url_complement=None):
    for element in input_dict:
        if element["characterId"] == character_id:
            if url_complement is None:
                output_dict = element
            else:
                output_dict = element[url_complement]
    return json.dumps(output_dict)


@app.route('/v1/public/characters', methods=['GET'])
def getAllCharacters():
    return jsonify(input_dict)


@app.route('/v1/public/characters/<character_id>', methods=['GET'])
def getCharacterById(character_id):
    if errorHandling(character_id):
        output_json = searchOnJson(character_id)
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'



@app.route('/v1/public/characters/<character_id>/comics', methods=['GET'])
def getComicsBycharacter_id(character_id):
    if errorHandling(character_id):
        output_json = searchOnJson(character_id, "comics")
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


@app.route('/v1/public/characters/<character_id>/events', methods=['GET'])
def getEventsBycharacter_id(character_id):
    if errorHandling(character_id):
        output_json = searchOnJson(character_id, "events")
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


@app.route('/v1/public/characters/<character_id>/series', methods=['GET'])
def getSeriesBycharacter_id(character_id):
    if errorHandling(character_id):
        output_json = searchOnJson(character_id, "series")
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


@app.route('/v1/public/characters/<character_id>/stories', methods=['GET'])
def getStoriesBycharacter_id(character_id):
    if errorHandling(character_id):
        output_json = searchOnJson(character_id, "stories")
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


if __name__ == "__main__":
    app.run(debug=True)
