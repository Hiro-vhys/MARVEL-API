from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

with open('MarvelApi.json', 'r') as marvelApi:
    input_json = marvelApi.read()

input_dict = json.loads(input_json)

@app.route('/', methods=['GET'])
def defaultRoute():
    index = '<h1>Endpoints disponiveis</h1><br>'
    index += '<p>characterId 1, 2, 3, 4 or 5</p>'
    index += '<p>/v1/public/characters</p>'
    index += '<p>/v1/public/characters/characterId/comics</p>'
    index += '<p>/v1/public/characters/characterId/events</p>'
    index += '<p>/v1/public/characters/characterId/series</p>'
    index += '<p>/v1/public/characters/characterId/stories</p>'
    return index

@app.route('/v1/public/characters', methods=['GET'])
def getAllCharacters():
    return jsonify(input_dict)


@app.route('/v1/public/characters/<characterId>', methods=['GET'])
def getCharacterById(characterId):
    if type(characterId) == int:
        if characterId > 0 and characterId < 6:
            for element in input_dict:
                if element["characterId"] == characterId:
                    output_dict = element
            output_json = json.dumps(output_dict)
            return jsonify(output_json)
        else:
            return '<p>Enter a number between 1 and 5</p>'
    else:
        return '<p>Only integers are allowed</p>'


@app.route('/v1/public/characters/<characterId>/comics', methods=['GET'])
def getComicsByCharacterId(characterId):
    if type(characterId) == int:
        if characterId > 0 and characterId < 6:
            for element in input_dict:
                if element["characterId"] == characterId:
                    output_dict = element["comics"]
            output_json = json.dumps(output_dict)
            return jsonify(output_json)
        else:
            return '<p>Enter a number between 1 and 5</p>'
    else:
        return '<p>Only integers are allowed</p>'


@app.route('/v1/public/characters/<characterId>/events', methods=['GET'])
def getEventsByCharacterId(characterId):
    if type(characterId) == int:
        if characterId > 0 and characterId < 6:
            for element in input_dict:
                if element["characterId"] == characterId:
                    output_dict = element["events"]
            output_json = json.dumps(output_dict)
            return jsonify(output_json)
        else:
            return '<p>Enter a number between 1 and 5</p>'
    else:
        return '<p>Only integers are allowed</p>'


@app.route('/v1/public/characters/<characterId>/series', methods=['GET'])
def getSeriesByCharacterId(characterId):
    if type(characterId) == int:
        if characterId > 0 and characterId < 6:
            for element in input_dict:
                if element["characterId"] == characterId:
                    output_dict = element["series"]
            output_json = json.dumps(output_dict)
            return jsonify(output_json)
        else:
            return '<p>Enter a number between 1 and 5</p>'
    else:
        return '<p>Only integers are allowed</p>'


@app.route('/v1/public/characters/<characterId>/stories', methods=['GET'])
def getStoriesByCharacterId(characterId):
    if type(characterId) == int:
        if characterId > 0 and characterId < 6:
            for element in input_dict:
                if element["characterId"] == characterId:
                    output_dict = element["stories"]
            output_json = json.dumps(output_dict)
            return jsonify(output_json)
        else:
            return '<p>Enter a number between 1 and 5</p>'
    else:
        return '<p>Only integers are allowed</p>'


if __name__ == "__main__":
    app.run(debug=True)
