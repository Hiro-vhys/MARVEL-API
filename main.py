from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

with open('MarvelApi.json', 'r') as marvelApi:
    inputJson = marvelApi.read()

inputDict = json.loads(inputJson)


@app.route('/v1/public/characters', methods=['GET'])
def getAllCharacters():
    return jsonify(inputDict)


@app.route('/v1/public/characters/<characterId>', methods=['GET'])
def getCharacterById(characterId):
    for element in inputDict:
        if element["characterId"] == characterId:
            outputDict = element
    outputJson = json.dumps(outputDict)
    return jsonify(outputJson)


@app.route('/v1/public/characters/<characterId>/comics', methods=['GET'])
def getComicsByCharacterId(characterId):
    for element in inputDict:
        if element["characterId"] == characterId:
            outputDict = element["comics"]
    outputJson = json.dumps(outputDict)
    return jsonify(outputJson)


@app.route('/v1/public/characters/<characterId>/events', methods=['GET'])
def getEventsByCharacterId(characterId):
    for element in inputDict:
        if element["characterId"] == characterId:
            outputDict = element["events"]
    outputJson = json.dumps(outputDict)
    return jsonify(outputJson)


@app.route('/v1/public/characters/<characterId>/series', methods=['GET'])
def getSeriesByCharacterId(characterId):
    for element in inputDict:
        if element["characterId"] == characterId:
            outputDict = element["series"]
    outputJson = json.dumps(outputDict)
    return jsonify(outputJson)


@app.route('/v1/public/characters/<characterId>/stories', methods=['GET'])
def getStoriesByCharacterId(characterId):
    for element in inputDict:
        if element["characterId"] == characterId:
            outputDict = element["stories"]
    outputJson = json.dumps(outputDict)
    return jsonify(outputJson)


if __name__ == "__main__":
    app.run(debug=True)
