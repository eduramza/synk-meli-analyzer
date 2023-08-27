from flask import Flask
from api.routes import api_blueprint
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(api_blueprint)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
