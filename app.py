from flask import Flask, jsonify, request, make_response
import numpy as np
import os
from pathlib import Path
import rag_pipeline
import config

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]


def create_app(testing : bool = True):
    model_id = config.summerizer_model_id
    hf_auth_token = config.hf_token
    store_dir_path = config.store_dir_path

    llm = rag_pipeline.getModel(model_id, hf_auth_token)
    db = rag_pipeline.database(store_dir_path)
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def version_info():
        return jsonify([{
            'Version': '1.0', 
            'ServiceName': 'Custom RAG Pipeline', 
            'ServiceDescription': 'A Flask app that exposes a REST API for providing access to a customized RAG pipeline, leveraging Llama 2 LLM model for its operations.'
            }])

    @app.route('/infer', methods=["POST"])
    def pred_fun():
        # Get the JSON data from the request
        json_data = request.get_json()

        # Assuming the JSON contains a key called 'input_string'
        input_string = json_data.get('input_string', '')

        # Process the input_string (Here, let's just return it as uppercase)
        processed_string = rag_pipeline.generate_response(input_string, llm=llm, db=db)

        # Return the processed string as a JSON response
        return jsonify({'processed_string': processed_string})


    return app

