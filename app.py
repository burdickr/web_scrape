from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_info = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_info)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

   # Run the scrape function
   mars_data = scrape_mars.scrape()

   # Update the Mongo database using update and upsert=True
   mongo.db.collection.update({}, mars_data, upsert=True)

   # Redirect back to home page
   return redirect("/")
if __name__ == "__main__":
   app.run(debug=True)