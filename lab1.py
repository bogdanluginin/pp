from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello-world-<int:variant_number>', methods=['GET'])
def hello_world(variant_number):
    return jsonify({'message': f'Hello World {variant_number}'}), 200

if __name__ == '__main__':
    app.run(debug=True)
