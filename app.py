from flask import Flask, jsonify, request
from professor_info import get_professor_info

app = Flask(__name__)

@app.route('/professor', methods=['GET'])
def professor():
    # Fetch the professor name from request arguments
    professor_name = request.args.get('name')
    
    if not professor_name:
        return jsonify({"error": "Missing professor name"}), 400

    # Call your function
    info = get_professor_info(professor_name)
    
    # Return the result as JSON
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
