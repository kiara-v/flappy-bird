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

if __name__ == '__main__':
    # main()
    # app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)
    # app.debug = True
    app.run(debug=True)
