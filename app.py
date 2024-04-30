from flask import Flask, request, jsonify
from file_processor import process_file

app = Flask(__name__)

@app.route('/process_sql', methods=['POST'])
def process_sql():
    file = request.files['file']
    output_path = request.form.get('output_path', 'output.csv')
    try:
        response = process_file(file, output_path)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
