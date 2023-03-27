from flask import Flask, render_template
# from controllers.continent_controller import continent_blueprint
from controllers.visits_controller import visits_blueprint
from controllers.user_visits_controller import user_visits_blueprint
from controllers.continents_controller import continents_blueprint

app = Flask(__name__)

app.register_blueprint(continents_blueprint)
app.register_blueprint(visits_blueprint)
app.register_blueprint(user_visits_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)