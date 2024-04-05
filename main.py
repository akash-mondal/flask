from flask import Flask, jsonify, request
import os
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.json
    graph_data = data['graph']
    num_vertices = graph_data['num_vertices']
    edges = graph_data['edges']
    
    # Prepare input for Java code
    java_input = f"{num_vertices}\n{len(edges)}\n"
    for edge in edges:
        java_input += f"{edge['start']} {edge['end']} {edge['weight']}\n"

    # Call Java code as a subprocess
    process = subprocess.Popen(['java', 'Graph'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=java_input)

    if stderr:
        return jsonify({"error": stderr}), 400

    # Parse Java output
    output_lines = stdout.strip().split('\n')
    result = {}
    for line in output_lines[1:]:
        vertex, distance = map(int, line.split('\t\t'))
        result[vertex] = distance

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
