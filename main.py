import plotly.graph_objects as go
from flask import Flask, render_template
from pytrends.request import TrendReq

app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config["DEBUG"] = True

@app.route('/chart')
def chart():
    trend_dict = get_trend_data()   
    return render_template('index_chart.html', trend_data=trend_dict)

def get_trend_data():
    pytrend = TrendReq()

    kw_list = ['dog', 'cat']
    pytrend.build_payload(kw_list)
    trend_data = pytrend.interest_over_time()
    trend_dict = trend_data.to_dict(orient='records')

    return trend_dict

# @app.route("/")
# def index():
#     pytrends = TrendReq()
#     pytrends.build_payload(["dog", "cat"])
#     trends = pytrends.interest_over_time()
    

    
#     return render_template("index_chart.html", chart=fig)


if __name__ == "__main__":
    app.run()