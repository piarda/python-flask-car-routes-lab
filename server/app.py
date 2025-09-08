from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

@app.route('/<model>')
def show_model(model):
    # Normalize input to match case-insensitively
    model_lower = model.lower()
    # Create a lowercase version for comparion
    models_lower = [m.lower() for m in existing_models]

    if model_lower in models_lower:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"
    
if __name__ == '__main__':
    app.run(debug=True)
