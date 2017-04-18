"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

magic = ['I turn you into a frog', 'you will fall in love!', 'you will be alert!!!!!!!']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.<br> 
    <a href="/hello">Click here</a> to go to hello!<br>
    <a href="/magic">Click here for magic!</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    result1 = """
        <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <br>
          Choose your compliment:
          <select name="compliment">"""

    result2 = ""
    for compliment in AWESOMENESS:
        result2.append("<option value=/" %s /"> %s </option>" % (compliment, compliment.capitalize()))

    result3 = """          </select>
          <br><br>
          <input type="submit" value="Submit">
        </form>
        <hr>
        <form action="/magic">
          <h1>Get some magic</h1>
          What's your name? <input type="text" name="person">
          <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

    return result1 + result2 + result3

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!<br>
        <h1> A little magic!</h1>
        Hi, {player} {spell}!
      </body>
    </html>
    """.format(player=player, compliment=compliment, spell=choice(magic))


@app.route('/magic')
def magic_person():
    """Cast a spell on user"""

    player = request.args.get("person")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A little magic</title>
      </head>
      <body>
        Hi, {}, {}!
      </body>
    </html>
    """.format(player, choice(magic))


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
