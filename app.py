import os
import math
import io
import urllib
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from PIL import Image

app = Flask(__name__)

ROOT_DB_URI = os.environ.get('DB_ADDRESS')

app.config["MONGO_URI"] = ROOT_DB_URI

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    popularResults = mongo.db.recipes.find().sort('viewcount')[0:4]
    newestResults = mongo.db.recipes.find().sort('creation_time')[0:4]
    return render_template("home.html", recipes_popular=popularResults, recipes_new=newestResults)

@app.route('/recipes')
def search():
    category = request.args.get('category')
    search_term = request.form.get('search')

    # alters the search based on if a name search was performed, or a category filtering.
    if(search_term != None):
        results = mongo.db.recipes.find({'name': {'$regex': search_term, "$options": "$i"}})

    if(category != None):
        if(category == 'All'):
            results = mongo.db.recipes.find()
        else:
            results = mongo.db.recipes.find({'category': category})

    # calculate the number of needed pages.
    pageCount = math.ceil(results.count()/8)

    return render_template('recipes.html', recipes=results, totalResults=results.count(), pages=pageCount)

@app.route('/recipes/view/<ID>')
def recipe_page(ID):
    # just gets the recipe via ID, then increments the viewcount before rendering it.
    target_recipe = mongo.db.recipes.find_one({'_id': ObjectId(ID)})
    target_recipe.update({'viewcount':target_recipe['viewcount']+1})
    mongo.db.recipes.update_one({'_id': ObjectId(ID)}, {'$set':target_recipe})
    return render_template('recipe.html', recipe=target_recipe)


@app.route('/recipes/edit/<ID>')
def edit_recipe(ID):
    if(ID == 'new'):
        return render_template('edit.html', target_recipe=0)

    else:  # gets the recipe to be edited via its ID
        target = mongo.db.recipes.find_one({'_id': ObjectId(ID)})
        return render_template('edit.html', target_recipe=target)

@app.route('/insert-recipe/<ID_target>', methods=["POST"])
def insert_recipe(ID_target):
    # gets the request, then makes the necessary changes to the last_edit timestamp, along with casting the prep and cook times as integers.
    edited_recipe = request.form.to_dict()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    edited_recipe.update({'last_edit_time':current_time})
    edited_recipe.update({'prep_time':int(edited_recipe.get('prep_time'))})
    edited_recipe.update({'cook_time':int(edited_recipe.get('cook_time'))})

    # if the recipe has a valid start to ensure it is a string readable as a link by requests.get()
    if(edited_recipe.get('image_link')[0:7] == "http://" or edited_recipe.get('image_link')[0:8] == "https://"):
        # attempts to run a GET request to image link. If it fails, assume it is invalid.
        try:
            image_load_attempt = urllib.request.urlopen(edited_recipe.get('image_link'))
        except:
            edited_recipe.update({'image_link': "missingImage"})
        else:
            try:
                file_attempt = io.BytesIO(image_load_attempt.read())
            except:
                edited_recipe.update({'image_link': "missingImage"})
            else:
                try:
                    Image.open(file_attempt)
                except:
                    edited_recipe.update({'image_link': "missingImage"})
    else:
        edited_recipe.update({'image_link': "missingImage"})
    
    # if a new recipe is being created, initialises statistics before inserting
    if(ID_target == 'new'):
        edited_recipe.update({'creation_time':current_time})
        edited_recipe.update({'viewcount':0})
        recipes = mongo.db.recipes
        recipes.insert_one(edited_recipe)
        new_recipe = recipes.find_one({'name': request.form['name']})
        ID_target = new_recipe.get('_id')
        
    else:
        recipes = mongo.db.recipes
        recipes.update_one({'_id': ObjectId(ID_target)}, {'$set': edited_recipe})
    
    return redirect(url_for('recipe_page', ID=ID_target))


@app.route('/delete-recipe/<ID>')
def delete_recipe(ID):
    mongo.db.recipes.delete_one({'_id': ObjectId(ID)})
    return redirect(url_for('search', category='All'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))
            