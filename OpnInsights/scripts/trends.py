from pytrends.request import TrendReq as tr
import plotly.express as px
import pandas as pd
import seaborn as sns
import plotly
import kaleido
print("Setup complete")

class Trends:

    def getTrend(self, text):
        text = text.replace(r"\r\n", "\n")
        terms = text.split("\n")
        trend = tr(hl="en-US", tz=30)
        trend.build_payload(kw_list=terms)

        df = trend.interest_over_time()
        df["date"] = df.index

        col = list(df.columns)
        col.remove("date")
        col.remove("isPartial")
        col
        pt = px.line(df, x="date", y = col)
        fig = plotly.offline.plot(pt, include_plotlyjs=True, output_type='div')

        return [fig, df]

def execute(text):
    ob = Trends()
    output = ob.getTrend(text)

    return output