import random
from flask import Flask, request, render_template
from compareHands import compareHands

#Create a Flask class object
app = Flask(__name__)



@app.route('/')
def hello_human():
    return 'Hello, human'

@app.route('/rps', methods=['POST', 'GET'])
def rps():
    result = None
    if request.method == 'POST':
        userHand = request.form['rps']
        options = ['Rock', 'Paper', 'Scissor']
        pcHand = random.choice(options)
        result = compareHands(userHand, pcHand)

        return render_template('rps.html', result = result)
    else:
        return render_template('rps.html', result = result)


# def rps():
#     # Ask user to choose Rock, Paper or Scissor
#     userHand = input('Choose Rock, Paper or Scissor:')
#
#     # Choose Rock, Paper or Scissor at random
#     options = ['Rock', 'Paper', 'Scissor']
#     pcHand = random.choice(options)
#
#     # Compare user input to computer choice
#     result = compareHands(userHand, pcHand)
#
#     return result

if __name__ == '__main__':
    app.run(debug = True)
