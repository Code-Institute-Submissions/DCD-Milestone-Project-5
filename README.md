# Communal Cookbook

The project's purpose is to act as a digital recipe book, for the useage of a relatively small user-base and I to share recipes in an easily accesible and readable format.
This is to act as an alternative to clumsily sharing photos of the recipes or links to other sites that may not be accessible in different countries, or may be difficult to use from a variety of devices.
 
## Demo

A live version of this site is available [here](https://dcd-milestone-recipe-site.herokuapp.com/)

## UX

### Strategy

The aim of this project is to create a web app for an online communal cookbook for the purpose of sharing and updating recipes; with a clean and immediately readable design to better facilitate it's use during cooking while following the recipes; An easy to use recipe creation and editing interface; And a searchable and well designed database.

The first thing to tackle was researching how similar sites lay out their content and divide their recipes into categories. Using the information gleaned from this research stage, the wireframes were created following some of the design trends from these sites, along with my own personal tastes, as the site will most likely continue to be used by me and my friends and associates to share recipes.

After this, a database had to be designed and created to ensure the recipes could be stored in a sensible and efficient manner. To do this, the vital information for each recipe was decided upon, and then following that a template document was created on the MongoDB database.

### Scope

The minimum viable product for this project involves: A homepage for a recipe site, a browse page with selectable categories and a search function, a recipe creation/update/delete page that properly updates the databse and is simple to use, and a page to display the selected recipe. This will be achieved through the use of Flask templates and python calls of the database. In addition, the site must feature CSS styling appropriate to the content, and javascript to further enhance the resposiveness of the site.

### Structure

The site will make use of templates, as is appropriate for a flask app, in order to ensure common elements accross pages do not need to be recreated multiple times, nor edited repeatedly for a single change. This will be further extended to include flask for loops to ease construction of elements of a page, such as the individual recipes being displayed during a search.

The database is a document-based system, as this is what MongoDB provides, along with making the most sense for the chosen content, as each recipe would be stored as what amounts to a document anyway.

### Skeleton

#### Home Page

![Homepage Wireframe](static/design/wireframes/homepage.png)

##### Recipe List Page

![Recipe List Wireframe](static/design/wireframes/listpage.png)

#### Recipe Create/Edit Page

![Recipe Create/Edit Page Wireframe](static/design/wireframes/createrecipe.png)

#### Recipe Page

![Recipe Page Wireframe](static/design/wireframes/recipemain.png)

#### Database Diagram

![Database Diagram](static/design/diagrams/recipediagram.png)

### Surface

The colour palette for this project needs to be both clean and immediately readable, so contrasting colours will need to be utilised, but the colourscheme should be cohesive so as to not draw attention away from important regions of the page.

as such, this palette was chosen:

![Colour Palette](static/design/dcd_palette.png)

This clean and readable design should extend to the general design of the elements of the page.

#### User Stories & Breakdown Thereof

 - As a User, I want to be able to view a recipe and follow it to recreate the dish:
    - Find a select a recipe
    - Be taken to the recipe's page
    - Be able to see the ingredients needed for the recipe
    - Be able to easily read the methodology for the dish

 - As a User, I want to be able to search for a specific recipe on the site:
    - Be able to sort recipes by category
    - Be able to search for a recipe by a term or word
        - Be able to search in dish name or ingredients

 - As a User, I want to be able to add my own recipes to the site:
    - Click a button to be taken to a recipe creation page
    - Have clear and readable fields to enter the appropriate information
    - Be taken to the created recipe page after submitting the data

 - As a User, I want to be able to edit or delete existing recipes:
    - Click on a button on a recipe's page to be taken to an edit page
        - Essentially the recipe addition page, but with information already filled
            - (Would need to reference the recipe ID in the page somehow to ensure the edit works)
        - Altering information on this page and submitting should alter the information in the database.
    - Click on a delete button on a recipe's page to remove it entirely.
        - A conformation message should be used to prevent accidental deletions.

## Features

The site consists of a digital recipe book, allowing users to view a variety of recipes via their browser. 
The homepage features a short listing of the most viewed recipes and the most recently added ones, allowing users to stay up to date and provide them tantalising meal ideas. The search
page allows users to find a particular recipe by its name, or to filter recipes by a desired meal category. The edit page allows users to alter the recipes, or add their own and ensure that these changes are saved.
The delete button allows for the removal of recipes by users.
Finally, the Recipe page allows users to view the recipe in a clean and clear manner, to make it easier to follow when cooking.

### Changes From Design

## Technologies Used

- [TinyMCE](https://www.tiny.cloud/)
- [Bootstrap](https://getbootstrap.com/)
    - [JQuery](https://jquery.com/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [MongoDB](https://www.mongodb.com/cloud/atlas)
- [pyMongo](https://pymongo.readthedocs.io/en/stable/)
- [FontAwesome](https://fontawesome.com/)

## Testing

### Code Validation

### User Story Testing

### Interesting Bugs & Known Issues

#### Known Issues

There's a minor scaling bug when changing the viewport width, but I can't be certain what's causing it due to the inconsistency with which it has occured during my testing. Going to go out on a limb and say it might be a chrome scaling issue, though I doubt it.

## Deployment

- Had to set up heroku environment variables to login

## Credits

### Content

- https://stackoverflow.com/questions/29451208/set-default-value-for-select-html-element-in-jinja-template

### Media

- https://pixabay.com/photos/bread-baguettes-food-3803633/

### Acknowledgements

