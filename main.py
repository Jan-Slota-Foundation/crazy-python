from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin

import string

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
    return 'home of api',200

@app.route('/morse', methods=['GET','POST'])
@cross_origin()
def morse():
    if request.method == 'POST':
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
            '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.', ' ': '/'
            }
        morse_code = ''
        content = request.json
        for char in content['text'].upper():
            if char in morse_dict:
                morse_code += morse_dict[char] + " "
        
        return jsonify(morse_code),200
    return "try to post sumn",200

@app.route("/notes", methods=["GET", "POST"])
@cross_origin()
def music():
    notes_dict = {
        ' ':0, 'A':1, 'B':3, 'C':5, 'D': 6, 'E':8, 'F':9, 'G':11
    }

    frac_dict = {
        '1/2' : 2, '1/4': 1
    }

    content = request.json
    payload = []
    notes = content["notes"].split("-")
    for note in notes:
        if (len(note) == 3):
            pay_note = [notes_dict[note[0]], int(note[1]), int(note[2])]
            
        if (len(note) == 5):
            pay_note = [notes_dict[note[0]], int(note[1]), frac_dict[note[2] + note[3] + note[4]]]

        payload.append(pay_note) 

        payload_str = str(payload)  
        payload_str = payload_str.replace("[", "{")
        payload_str = payload_str.replace("]","}")
        print(payload_str)
    return jsonify(payload_str),200



if __name__=="__main__":
    app.run(debug=True, port=6942)
