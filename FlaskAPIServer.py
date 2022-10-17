import pandas as pd
from flask import Flask, render_template
from flask_restful import Api, Resource



sheet_id = '1BwbEBnjsBQQ46-FweVfNS8tA96B4Ic7xsZ9yr7bdr-8'
df =pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
records = df.to_dict(orient='records')


# Instantiate New Flask APP Object
app = Flask(__name__)

# Intialize API object for the Flask Application
api = Api(app)


# Routes aka Pages
@app.route('/')
def index():
    return render_template('index.html')

# API request
class All(Resource):

    def get(self):
        return records


# Register API Resources
api.add_resource(All, '/api/')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)