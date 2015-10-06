from flask import Flask, request

# from random import choice


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    
    <!DOCTYPE html>
    <html>
        <head>
            <title>Homepage</title>
        </head>
        <body>
            <p>Hi! This is the home page.</p>
            <p><a href="/hello">Click here for a greeting!</a></p>
        </body>
    </html>
    """

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet" method="POST">
                <label>What's your name? <input type="text" name="person"></label>
                <input type="submit"><br>
                Compliment:
                <select name="compliment">
                        <option value='awesome'>Awesome</option>
                        <option value='terrific'>Terrific</option>
                        <option value='fantastic'>Fantastic</option>
                        <option value='neato'>Neato</option>
                        <option value='fantabulous'>Fantabulous</option>
                        <option value='wowza'>Wowza</option>
                        <option value='oh-so-not-meh'>Oh-So-Not-Meh</option>
                        <option value='brilliant'>Brilliant</option>
                        <option value='ducky'>Ducky</option>
                        <option value='coolio'>Coolio</option>
                        <option value='incredible'>Incredible</option>
                        <option value='wonderful'>Wonderful</option>
                        <option value='smashing'>Smashing</option>
                        <option value='lovely'>Lovely</option>
                </select>
            </form>
        </body>
    </html>

    """

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form.get("person")
    compliment = request.form.get("compliment")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    app.run(debug=True)

    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
