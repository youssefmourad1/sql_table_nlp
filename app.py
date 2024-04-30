from flask import Flask, request, jsonify
from file_processor import process_file
import pandas as pd

app = Flask(__name__)

@app.route('/process_sql', methods=['POST'])
def process_sql():
    file = request.files['file']
    output_path = request.form.get('output_path', 'output.csv')
    try:
        df, response = process_file(file, output_path)  # Adjusted to receive df and response
        # Convert DataFrame to JSON
        df_json = df.to_json(orient='records', lines=True)
        # Include DataFrame JSON in response
        response['data'] = df_json
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
