from app import app

@app.route('/')
def index():
    return "Hello yeeeyy!"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"