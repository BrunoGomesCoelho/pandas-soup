import pickle
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<input>')
def hello_name(input):
    # Read encoder and classifier
    brand_enc = pickle.load(open("Brand", "rb"))
    clf = pickle.load(open("classificador", "rb"))

    brand, price = input.split("-")

    brand_label = brand_enc.transform([brand])[0]
    price = float(price)
    
    print(brand_label, price)

    pred = clf.predict([[brand_label, price]])


    return "Hello {}!".format(pred)


if __name__ == '__main__':
    app.run()
