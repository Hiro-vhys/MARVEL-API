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
    index += '/v1/public/characters/character_id'
    index += '<p>/v1/public/characters/character_id/comics</p>'
    index += '<p>/v1/public/characters/character_id/events</p>'
    index += '<p>/v1/public/characters/character_id/series</p>'
    index += '<p>/v1/public/characters/character_id/stories</p>'
    return index

@app.route('/v1/public/characters', methods=['GET'])
def getAllCharacters():
    return jsonify(input_dict)


@app.route('/v1/public/characters/<character_id>', methods=['GET'])
def getCharacterById(character_id):
    if character_id.isdecimal() and 0 < int(character_id) < 6:
        for element in input_dict:
            if element["characterId"] == character_id:
                output_dict = element
        output_json = json.dumps(output_dict)
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'



@app.route('/v1/public/characters/<character_id>/comics', methods=['GET'])
def getComicsBycharacter_id(character_id):
    if character_id.isdecimal() and 0 < int(character_id) < 6:
        for element in input_dict:
            if element["characterId"] == character_id:
                output_dict = element["comics"]
        output_json = json.dumps(output_dict)
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


@app.route('/v1/public/characters/<character_id>/events', methods=['GET'])
def getEventsBycharacter_id(character_id):
    if character_id.isdecimal() and 0 < int(character_id) < 6:
        for element in input_dict:
            if element["characterId"] == character_id:
                output_dict = element["events"]
        output_json = json.dumps(output_dict)
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


@app.route('/v1/public/characters/<character_id>/series', methods=['GET'])
def getSeriesBycharacter_id(character_id):
    if character_id.isdecimal() and 0 < int(character_id) < 6:
        for element in input_dict:
            if element["characterId"] == character_id:
                output_dict = element["series"]
        output_json = json.dumps(output_dict)
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


@app.route('/v1/public/characters/<character_id>/stories', methods=['GET'])
def getStoriesBycharacter_id(character_id):
    if character_id.isdecimal() and 0 < int(character_id) < 6:
        for element in input_dict:
            if element["characterId"] == character_id:
                output_dict = element["stories"]
        output_json = json.dumps(output_dict)
        return jsonify(output_json)
    else:
        return '<p>Enter a number between 1 and 5</p>'


if __name__ == "__main__":
    app.run(debug=True)
