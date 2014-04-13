from flask import Flask
from flask import render_template
import pickle

app = Flask(__name__)

#path = ""
path = "/home/dhistory/webapps/inaword/inaword/"

@app.route("/")
def home():
	with open(path + 'words_data.pickle', 'rb') as data_file:
		data = pickle.load(data_file)
	return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)