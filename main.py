from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

with open('MarvelApi.json', 'r') as MarvelApi:
    input_json = MarvelApi.read()

input_dict = json.loads(input_json)


@app.route('/v1/public/characters', methods=['GET'])
def getAllCharacters():
    return jsonify(input_dict)


@app.route('/v1/public/characters/<characterId>', methods=['GET'])
def getCharacterById(characterId):
    for element in input_dict:
        if element["characterId"] == characterId:
            output_dict = element
    output_json = json.dumps(output_dict)
    return output_json


@app.route('/v1/public/characters/<characterId>/comics', methods=['GET'])
def getComicsByCharacterId(characterId):
    for element in input_dict:
        if element["characterId"] == characterId:
            output_dict = element["comics"]
    output_json = json.dumps(output_dict)
    return output_json


@app.route('/v1/public/characters/<characterId>/events', methods=['GET'])
def getEventsByCharacterId(characterId):
    for element in input_dict:
        if element["characterId"] == characterId:
            output_dict = element["events"]
    output_json = json.dumps(output_dict)
    return output_json


@app.route('/v1/public/characters/<characterId>/series', methods=['GET'])
def getSeriesByCharacterId(characterId):
    for element in input_dict:
        if element["characterId"] == characterId:
            output_dict = element["series"]
    output_json = json.dumps(output_dict)
    return output_json


@app.route('/v1/public/characters/<characterId>/stories', methods=['GET'])
def getStoriesByCharacterId(characterId):
    for element in input_dict:
        if element["characterId"] == characterId:
            output_dict = element["stories"]
    output_json = json.dumps(output_dict)
    return output_json


if __name__ == "__main__":
    app.run(debug=True)
