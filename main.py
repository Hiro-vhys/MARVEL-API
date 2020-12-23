from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)

with open('.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

@app.route('/v1/public/characters', methods=['GET'])
def getAllCharacters():
    return jsonify(obj)

@app.route('/v1/public/characters/{characterId}', methods=['GET'])
def getCharactersById(charactersId):
    return jsonify(obj)

@app.route('/v1/public/characters/{characterId}/comics', methods=['GET'])
def getComicsByCharactersId(charactersId):
    return jsonify(obj)

@app.route('/v1/public/characters/{characterId}/events', methods=['GET'])
def getEventsByCharactersId(charactersId):
    return jsonify(obj)

@app.route('/v1/public/characters/{characterId}/series', methods=['GET'])
def getSeriesByCharactersId(charactersId):
    return

@app.route('/v1/public/characters/{characterId}/stories', methods=['GET'])
def getStoriesByCharactersId(charactersId):
    return


if __name__ == "__main__":
    app.run(debug=True)