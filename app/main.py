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
    return jsonify({"recipes": json_recipes})

@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    new_recipe = Recipe(name=data['name'], ingredients=data['ingredients'], instructions=data['instructions'])

    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"message": "Recipe created successfully"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)