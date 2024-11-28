from flask import Flask,request
from B2BDao import validateInputAccountValidation,postTran

app = Flask(__name__)

@app.route("/getSampleData")
def hello():
    return "Welcome to B2B Python Service"

@app.route("/EquityB2B/validate",methods=['POST'])
def validateAccount():
    try:
        return validateInputAccountValidation(request.get_data())
    except Exception as e:
        return "Error___"+str(e)

@app.route("/EquityB2B/notification",methods=['POST'])
def postTransaction():
    return postTran(request.get_data())

#To run the app on WSGI server START
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=18002)
    print('Sertver Started')
#To run the app on WSGI server START
