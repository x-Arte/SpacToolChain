from flask_cors import CORS
from web import create_app
from flask import Flask, jsonify, request, make_response
app = create_app()
#Access-Control-Allow-Origin
CORS(app, resources={r"/*": {"origins": "*"}}, cors_allow_methods=['GET', 'POST'], allow_headers="*", supports_credentials=True)
@app.route('/hello', methods=["GET"])
def hello_world(): # put application's code here
    return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
