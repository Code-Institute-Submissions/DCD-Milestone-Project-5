import os
import math
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# creating flask instance
app = Flask(__name__)

# Local environement variables, for security.
ROOT_DB_URI = os.environ.get('DB_ADDRESS')

app.config["MONGO_URI"] = ROOT_DB_URI

# pyMongo Constructor
mongo = PyMongo(app)


# app routes
@app.route('/')
@app.route('/home')
def home():
    # Gets the 4 most popular results by checking their viewcounts
    popResults = mongo.db.recipes.find().sort('viewcount')[0:4]
    
    # and this gets the 4 most recently created recipes, rather than most recently edited.
    newResults = mongo.db.recipes.find().sort('creation_time')[0:4]
    return render_template("home.html", recipes_popular=popResults, recipes_new=newResults)

# route for the recipe search page.
@app.route('/recipes')
def search():
    # Gets the search data, and takes the search value from it.
    category = request.args.get('category')
    keyword = request.form.get('search')

    # checks the type of the query, if it's a name does a simple search to find any names that contain the string.
    if(keyword != None):
        results = mongo.db.recipes.find({'name': {'$regex': keyword, "$options": "$i"}})

    # if it's a category, checks if it is for all recipes, and passes them to results. Otherwise, it searches for matching recipes via the category field.
    if(category != None):
        if(category == 'All'):
            results = mongo.db.recipes.find()
        else:
            results = mongo.db.recipes.find({'category': category})

    # calculate the number of needed pages.
    pageCount = math.ceil(results.count()/8)

    # passes the search results, the number of those results, and the needed number of pages to the template.
    return render_template('recipes.html', recipes=results, totalResults=results.count(), pages=pageCount)

# route for viewing a recipe's page.
@app.route('/recipes/view/<ID>')
def recipe_page(ID):
    # just gets the recipe via ID, then increments the viewcount before rendering it.
    target_recipe = mongo.db.recipes.find_one({'_id': ObjectId(ID)})
    target_recipe.update({'viewcount':target_recipe['viewcount']+1})
    mongo.db.recipes.update_one({'_id': ObjectId(ID)}, {'$set':target_recipe})
    return render_template('recipe.html', recipe=target_recipe)


# route for the recipe editpage.
@app.route('/recipes/edit/<ID>')
def edit_recipe(ID):
    if(ID == 'new'):  # called when editing a new recipe, obviously. Simply passes a value to the page to show this.
        return render_template('edit.html', target_recipe=0)

    else:  # gets the recipe to be edited via its ID
        target = mongo.db.recipes.find_one({'_id': ObjectId(ID)})
        return render_template('edit.html', target_recipe=target)

# Route for adding a recipe to the database, or updating an existing one.
@app.route('/insert-recipe/<ID_target>', methods=["POST"])
def insert_recipe(ID_target):
    # gets the request, then makes the necessary changes to the last_edit time, along with casting the prep and cook times as integers.
    edited_recipe = request.form.to_dict()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    edited_recipe.update({'last_edit_time':current_time})
    edited_recipe.update({'prep_time':int(edited_recipe.get('prep_time'))})
    edited_recipe.update({'cook_time':int(edited_recipe.get('cook_time'))})

    # if the recipe is new, adds a creation time alongside a viewcount to the request form, then inserts it into the database. Also gets the newly added entry's ID for redirection.
    if(ID_target == 'new'):
        edited_recipe.update({'creation_time':current_time})
        edited_recipe.update({'viewcount':0})
        recipes = mongo.db.recipes
        recipes.insert_one(edited_recipe)
        new_recipe = recipes.find_one({'name': request.form['name']})
        ID_target = new_recipe.get('_id')

    # Just updates the targeted recipe, nothing fancy.
    else:
        recipes = mongo.db.recipes
        recipes.update_one({'_id': ObjectId(ID_target)}, {'$set': edited_recipe})

    # redirects to the edited/created recipe's page.
    return redirect(url_for('recipe_page', ID=ID_target))

# just deletes the targeted recipe.
@app.route('/delete-recipe/<ID>')
def delete_recipe(ID):
    mongo.db.recipes.delete_one({'_id': ObjectId(ID)})
    return redirect(url_for('search', category='All'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))
