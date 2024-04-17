# main routes/endpoints
from flask import request, jsonify
from config import app,db
from models import Recipe

#GET ALL
@app.route('/recipes', methods={"GET"})
def get_recipes():
    recipes = Recipe.query.all()
    # converting to json since it is an object
    json_recipes = list(map(lambda x: x.to_json(), recipes))
    return jsonify({"recipes": json_recipes}), 200

# Get by ID
@app.route('/recipes/<int:id>', methods=["GET"])
def get_recipe(id):
    recipe = Recipe.query.get_or_404(id)

    if not recipe:
        return jsonify({"message": "Recipe not found!"}), 404
    
    return jsonify(recipe.to_json()), 200 

# ADD a recipe
@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    new_recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'])

    # adding it to our model
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"message": "Recipe created successfully"})

#update recipe by ID
@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    data = request.json
    recipe.name = data['name']
    recipe.ingredients = data['ingredients']
    recipe.insturctions = data['instructions']

    db.session.commit()
    return jsonify({"message": "Recipe updated successfuly!"})

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get_or_404(id)

    # delete found recipe
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Recipe deleted successfully!"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)