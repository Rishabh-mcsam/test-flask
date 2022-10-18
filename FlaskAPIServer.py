import pandas as pd
from flask import Flask, render_template
from flask_restful import Api, Resource


df =pd.read_csv("https://docs.google.com/spreadsheets/d/1BwbEBnjsBQQ46-FweVfNS8tA96B4Ic7xsZ9yr7bdr-8/export?format=csv")
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
        df =pd.read_csv("https://docs.google.com/spreadsheets/d/1BwbEBnjsBQQ46-FweVfNS8tA96B4Ic7xsZ9yr7bdr-8/export?format=csv")
        records = df.to_dict(orient='records')
        return records


# Register API Resources
api.add_resource(All, '/api/')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)