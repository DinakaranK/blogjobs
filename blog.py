import flask,sys,time
from flask import Flask, render_template, request,make_response
from flask import request, jsonify,json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/score/', methods=['GET','POST'])
def result():
    return 'trillionaire'
    
if __name__ == '__main__':
    app.run(debug=True)