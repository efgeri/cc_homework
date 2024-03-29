from flask import Flask, render_template
# from controllers.continent_controller import continent_blueprint
from controllers.visits_controller import visits_blueprint
from controllers.user_visits_controller import user_visits_blueprint
from controllers.continents_controller import continents_blueprint
from controllers.countries_controller import countries_blueprint
from controllers.cities_controller import cities_blueprint
from controllers.users_controller import users_blueprint
import repositories.user_repository as user_repo

app = Flask(__name__)

app.register_blueprint(continents_blueprint)
app.register_blueprint(visits_blueprint)
app.register_blueprint(user_visits_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)

@app.route('/')
def home():
    every_user = user_repo.select_all()
    return render_template('index.html', every_user = every_user)

if __name__ == '__main__':
    app.run(debug=True)