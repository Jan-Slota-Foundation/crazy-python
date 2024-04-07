from flask import Flask,request


app = Flask(__name__)

@app.route('/')
def home():
    return 'home of api'

@app.route('/morse', methods=['GET','POST'])
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
        print(content['text'])
        for char in content['text'].upper():
            if char in morse_dict:
                morse_code += morse_dict[char] + " "
        
        return morse_code
    return "ahoj fungujem"

@app.route("/notes", methods=["GET", "POST"])
def music():
    return 'milan!'



if __name__=="__main__":
    app.run(debug=True, port=6942)
