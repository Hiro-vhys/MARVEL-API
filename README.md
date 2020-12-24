# MARVEL-API
## Re-implement the Marvel Api endpoints so that it can be accessed even when offline.

<p>
 <a href="#objetivo">objective</a> •
 <a href="#how to use">how to use</a> •
 <a href="#tecnologias">Technology</a> •
 <a href="#autor">Author</a>
</p>

## Endpoints implemented:
- `/v1/public/characters`
- `/v1/public/characters/<characterId>`
- `/v1/public/characters/<characterId>/comics`
- `/v1/public/characters/<characterId>/events`
- `/v1/public/characters/<characterId>/series`
- `/v1/public/characters/<characterId>/stories`

### Prerequisites:

Before you begin, you will need to have the following tools installed on your machine:
[Python3.9](https://www.python.org/), Flask, pip.
In addition, it is good to have an editor/IDE to work with the code like [VSCode](https://code.visualstudio.com/) and [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=linux) 

### Install the dependencies:
* Installing pip for Python 3  `$ sudo apt install python3-pip`
* Installing Python            `$ sudo apt install python3.8`
* Installing Flask             `$ sudo pip install Flask`

### Clone this repository:
$ git clone <https://github.com/Hiro-vhys/MARVEL-API.git>

### Run the application:
$ FLASK_APP=main.py flask run

### The server will start at port: 5000 - go to <http://127.0.0.1:5000>

### Tools used:
- Operational system: Ubuntu
- IDE: PyCharm
- Microframework:
    - Flask
- Language:
    - Python

### Author:
Victor Hiroshi  
May the force be with us 👋🏽 
[![Linkedin Badge](https://img.shields.io/badge/-Victor-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/victor-santos-009086178/)](https://www.linkedin.com/in/victor-santos-009086178/) 
