from flask import Flask
<<<<<<< HEAD

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    return("index.html")

if __name__ == "__main__":
    app.run()
=======
>>>>>>> 843ddee7f87919cf66abe8087f2ebb639d2968b4
