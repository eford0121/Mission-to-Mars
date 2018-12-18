from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import pymongo
import scrape_mars

app = Flask(__name__)

#create connection variable

conn = 'mongodb://localhost:27017/mars_db'
#pass connection to the pymongo instance
client = pymongo.MongoClient(conn)
#connection to database
db = client.mars_db
#drops collection if available to remove duplicates
db.mars.drop()
collection = db.mars

@app.route("/")
def index():
    mars_data = list(db.collection.find())[0]
    return render_template ("index.html", mars_data = mars_data)

@app.route("/scrape")
def scrape ():
    mars_data = scrape_mars.scrape()
    db.collection.insert_one(mars_data)
    return render_template('scrape.html')


if __name__ == "__main__":
    app.run(debug=True)




