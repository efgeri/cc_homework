from flask import Flask, render_template
# from controllers.continent_controller import continent_blueprint
from controllers.visits_controller import visits_blueprint
from controllers.user_visits_controller import user_visits_blueprint
from controllers.continents_controller import continents_blueprint
from controllers.users_controller import users_blueprint
import repositories.user_repository as user_repo

app = Flask(__name__)

app.register_blueprint(continents_blueprint)
app.register_blueprint(visits_blueprint)
app.register_blueprint(user_visits_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    all_users = user_repo.select_all()
    return render_template('index.html', all_users = all_users)

if __name__ == '__main__':
    app.run(debug=True)