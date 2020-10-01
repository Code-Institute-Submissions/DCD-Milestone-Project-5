import os
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
    popResults = mongo.db.recipes.find().sort('viewcount')[0:4]
    print(popResults)
    newResults = mongo.db.recipes.find().sort('creation-time')[0:4]
    return render_template("home.html", recipes_popular=popResults, recipes_new=newResults)


@app.route('/recipes/<category>')
def recipe_search(category):
    if(category == 'All'):
        searchResults = mongo.db.recipes.find()
        return render_template('recipes.html', recipes=searchResults)

    else:
        searchResults = mongo.db.recipes.find({'category': category})
        return render_template('recipes.html', recipes=searchResults)


@app.route('/recipes')
def name_search():
    searchString = format(request.args.get('search'))
    results = mongo.db.recipes.find({'recipe_name': {'$regex': searchString, "$options": "$i"}})
    return render_template('recipes.html', recipes=results)


@app.route('/recipes/view/<ID>')
def recipe_page(ID):
    target_recipe = mongo.db.recipes.find_one({'_id': ObjectId(ID)})
    target_recipe.update({'viewcount':target_recipe['viewcount']+1})
    mongo.db.recipes.update_one({'_id': ObjectId(ID)}, {'$set':target_recipe})
    return render_template('recipe.html', recipe=target_recipe)


@app.route('/recipes/edit/<ID>')
def edit_recipe(ID):
    if(ID == 'new'):  # this is called when attempting to create a new recipe
        return render_template('edit.html', target_recipe=0)

    else:  # this is called when editing an existing one
        target = mongo.db.recipes.find_one({'_id': ObjectId(ID)})
        return render_template('edit.html', target_recipe=target)


@app.route('/insert-recipe/<ID_target>', methods=["POST"])
def insert_recipe(ID_target):
    edited_recipe = request.form.to_dict()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    edited_recipe.update({'last-edit-time':current_time})
    if(ID_target == 'new'):
        edited_recipe.update({'creation-time':current_time})
        edited_recipe.update({'viewcount':0})
        recipes = mongo.db.recipes
        recipes.insert_one(edited_recipe)
        new_recipe = recipes.find_one({'recipe_name': request.form['recipe_name']})
        ID_target = new_recipe.get('_id')
    else:
        recipes = mongo.db.recipes
        recipes.update_one({'_id': ObjectId(ID_target)}, {'$set': edited_recipe})

    return redirect(url_for('recipe_page', ID=ID_target))


@app.route('/delete-recipe/<ID>')
def delete_recipe(ID):
    mongo.db.recipes.delete_one({'_id': ObjectId(ID)})
    return redirect(url_for('recipe_search', category='All'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)  # remove debug for release version
