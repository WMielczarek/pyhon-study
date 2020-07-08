from flask import Flask, jsonify, request, abort
import jsonUtils


app = Flask(__name__)

choose = 'memory'
#choose = 'file'

if choose == 'memory':
    print("Working on memory")
    offerts = {'OFFERTS': [
        {"ID": '1',
         "Title": 'Wyjazd',
         'Driver': "Henryk",
         "Departure": "Szczecin",
         "Destination": "Zielona Góra",
         "Departure date": "12/06/2018",
         "Departure time": "11.00",
         "Added": "25/05/2018",
         "Rating": '4'
         },
        {"ID": '2',
         "Title": 'Odjazd',
         'Driver': "Wojtek",
         "Departure": "Wroclaw",
         "Destination": "Warszawa",
         "Departure date": "12/06/2018",
         "Departure time": "13.00",
         "Added": "26/05/2018",
         "Rating": '4'
         },
        {"ID": '3',
         "Title": 'Ruszamy',
         "Driver": "Katarzyna",
         "Departure": "Gdynia",
         "Destination": "Międzyzdroje",
         "Departure date": "11/07/2018",
         "Departure time": "14.00",
         "Added": "25/06/2018",
         "Rating": '6'
         },
        {"ID": '4',
         "Title": 'Jedzmy',
         'Driver': "KrzysiekK",
         "Departure": "Poznan",
         "Destination": "Wroclaw",
         "Departure date": "15/06/2018",
         "Departure time": "10.00",
         "Added": "22/05/2018",
         'Rating': '6',
         }
    ]}
else:
    print("Working on file")
    offerts = jsonUtils.loadJson('OFFERTS')


@app.route('/', methods=['GET'])
def firstPage():
    return jsonify('It works! Home page.')



@app.route('/offerts', methods=['GET'])
def getAll():
    return jsonify(offerts)


@app.route('/offerts/<string:title>', methods=['GET'])
def getOneByTitle(title):
    i = 0
    while i < len(offerts['OFFERTS']):
        if (offerts['OFFERTS'][i]['Title'] == title):
            found = offerts['OFFERTS'][i]
        i += 1
    return jsonify({'OFFERTS': found})


@app.route('/offerts/getOneID/<string:offertID>', methods=['GET'])
def getOneByID(offertID):
    i = 0
    while i < len(offerts['OFFERTS']):
        if (offerts['OFFERTS'][i]['ID'] == offertID):
            found = offerts['OFFERTS'][i]
        i += 1
    return jsonify({'OFFERTS': found})


@app.route('/offerts', methods=["POST"])
def createOffert():
    dat = {
        'ID': request.json['ID'],
        'Title': request.json['Title'],
        'Driver': request.json['Driver'],
        'Departure': request.json['Departure'],
        'Destination': request.json['Destination'],
        'Departure date': request.json['Departure date'],
        'Departure time': request.json['Departure time'],
        'Added': request.json['Added'],
        'Rating': request.json['Rating'],
    }
    offerts.append(dat)
    return jsonify(dat)


@app.route('/offerts/<string:offertID>', methods=['DELETE'])
def deleteOffert(offertID):
    em = [emp for emp in offerts if (emp['ID'] == offertID) ]
    if len(em) == 0:
        abort(404)

    offerts.remove(em[0])
    return jsonify({'response': 'Success'})



if __name__ == '__main__':
    app.run(debug=True, port=5000)
