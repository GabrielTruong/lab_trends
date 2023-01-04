from flask import Flask, render_template
from pytrends.request import TrendReq
import plotly.offline as offline

import plotly.express as px


app = Flask(__name__)

@app.route("/")
def index():
    pytrends = TrendReq()
    pytrends.build_payload(["machine learning", "deep learning"])
    trends = pytrends.interest_over_time()
    print(trends)
    return render_template("index.html", trends=trends)


@app.route("/chart")
def index():
    pytrends = TrendReq()
    pytrends.build_payload(["machine learning", "deep learning"])
    trends = pytrends.interest_over_time()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=trends.index, y=trends["machine learning"], name="ML"))
    fig.add_trace(go.Scatter(x=trends.index, y=trends["deep learning"], name="DL"))
    
    # Convert the chart to an HTML string
    chart_html = offline.plot(fig, include_plotlyjs=False, output_type="div")
    
    return render_template("index.html", chart_html=chart_html)

if __name__ == "__main__":
    app.run()