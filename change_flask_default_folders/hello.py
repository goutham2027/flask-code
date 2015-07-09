from flask import Flask
from flask import render_template

app = Flask(__name__,static_folder='assets',template_folder='templates_007',instance_path="full_path_to_instance_folder/instance_007", instance_relative_config=True)
app.config.from_pyfile('config.py')

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
