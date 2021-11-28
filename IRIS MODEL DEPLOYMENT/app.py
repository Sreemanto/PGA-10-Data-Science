from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iri_knn.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    input_1 = request.form['sepal_length']
    input_2 = request.form['sepal_width']
    input_3 = request.form['petal_length']
    input_4 = request.form['petal_width']

    arr = np.array([[input_1, input_2, input_3, input_4]])

    pred = model.predict(arr)

    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
