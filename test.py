from pytrends.request import TrendReq
import streamlit as st

pytrends = TrendReq()
pytrends.build_payload(["machine learning", "deep learning"])
trends = pytrends.interest_over_time()

st.title("Trends")
st.area_chart(trends,rotation=90)