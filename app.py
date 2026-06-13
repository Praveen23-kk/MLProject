from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData

application = Flask(__name__)
app = application

# Module-level cache — pipeline loaded only once, on first request
_predict_pipeline = None

def get_pipeline():
    global _predict_pipeline
    if _predict_pipeline is None:

        from src.pipeline.predict_pipeline import PredictPipline
        _predict_pipeline = PredictPipline()
    return _predict_pipeline

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')


    from src.pipeline.predict_pipeline import CustomData

    data = CustomData(
        gender=request.form.get('gender'),
        race_ethnicity=request.form.get('ethnicity'),
        parental_level_eduction=request.form.get('parental_level_of_education'),
        lunch=request.form.get('lunch'),
        test_preparation_course=request.form.get('test_preparation_course'),
        reading_score=float(request.form.get('reading_score')),
        wrinting_score=float(request.form.get('writing_score'))
    )

    pred_df = data.get_data_as_data_frame()
    results = get_pipeline().predict(pred_df)
    return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0",Debug=True)