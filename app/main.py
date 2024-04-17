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


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)