from flask import Flask, request, jsonify
import pandas as pd
from file_processor import *

app = Flask(__name__)

@app.route('/process_sql', methods=['POST'])
def process_sql():
    data = request.get_json()
    file_path = data.get('file')
    
    if not file_path:
        return jsonify({'error': 'No file path provided'}), 400
    
    output_path = request.args.get('output_path', 'output.csv')
    
    try:
        with open(file_path, 'rb') as file:
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
