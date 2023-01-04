import plotly.graph_objects as go
from flask import Flask, render_template
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route("/")
def index():
    pytrends = TrendReq()
    pytrends.build_payload(["dog", "cat"])
    trends = pytrends.interest_over_time()
    
    # Create a line chart using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=trends.index, y=trends["dog"], name="Dog"))
    fig.add_trace(go.Scatter(x=trends.index, y=trends["cat"], name="Cat"))
    
    return render_template("index_chart.html", chart=fig)


if __name__ == "__main__":
    app.run()