import os
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv

# Setting up flask
app = Flask(__name__)

# Loading dotenv
load_dotenv(dotenv_path='./.env')

# Getting the username and password from .env file
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

# Connecting to Mongo Atlas
URI = "mongodb+srv://{}:{}@assignment2cluster.5lvu5.mongodb.net/?retryWrites=true&w=majority&ssl=true&appName=assignment2Cluster".format(MONGO_USERNAME, MONGO_PASSWORD)

# Print Error Message
if (MONGO_PASSWORD == None or MONGO_USERNAME == None):
    print("Connection Error: Please create .env file and enter your MongoDB Username and password")

client = MongoClient(URI)
db = client.shop_db
products_collection = db.products


# Routing to / to render home.html
@app.route("/")
def home():
    return render_template('home.html')

# Routing to /products to render Products and display the products from the mongodb shop_db database
@app.route("/products")
def products():
    products = products_collection.find()
    return render_template("products.html", products = products)

if __name__ == '__main__':
    app.run()
