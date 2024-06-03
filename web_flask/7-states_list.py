#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    states = storage.all(State)
    dict_states = {}
    for _, value in states.items():
        dict_states[value.id] = value.name
    return render_template('7-states_list.html', states=dict_states)


@app.teardown_appcontext
def storage_close(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
