from flask import Flask, render_template, request
from graph import load_graph, a_star

app = Flask(__name__)

# Define positions of places (x, y) in pixels
positions = {
    "College Gate": (870, 131),
    "Anviksha": (763, 187),
    "SOT": (611, 262),
    "Temple": (920, 307),
    "Aangnva Ground": (511, 321),
    "Hostel": (423, 414),
    "SOM Building": (927, 587)
}

@app.route('/')
def index():
    places = list(positions.keys())
    return render_template('index.html', places=places)

@app.route('/find_path', methods=['POST'])
def find_path():
    start = request.form.get('start')
    end = request.form.get('end')

    if not start or not end:
        return "Start and End locations required", 400

    graph = load_graph()
    path = a_star(graph, positions, start, end)

    return render_template(
        'directions.html',
        path=path,
        positions=positions,
        start=start,
        end=end
    )

if __name__ == '__main__':
    app.run(debug=True)