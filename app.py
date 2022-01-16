"""
Entrance of the program.
"""
from game import *
import random

from flask import Flask

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route("/")
def main():
    random.seed(RANDOM_SEED)
    game = Game()
    while game.running and game.current_generation < N_GEN:
        game.reset()
        game.run()

@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404

if __name__ == '__main__':
    # main()
    # app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
    # app.debug = True
    app.run(debug=True)
