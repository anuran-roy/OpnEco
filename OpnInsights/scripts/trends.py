from pytrends.request import TrendReq as tr
import plotly.express as px
import pandas as pd
# import seaborn as sns
import plotly
# import kaleido
import time
# print("Setup complete")

class Trends:

    def getTrend(self, text):
        text = text.replace(r"\r\n", "\n")
        terms = text.split("\n")
        i = 0
        br = []
        while(i<len(terms)):
            br.append(terms[i:i+4])
            i+=4
        try:
            df = pd.DataFrame()
            dft = pd.DataFrame()
            for i in range(len(br)):
                trend = tr(hl="en-US", tz=365)
                trend.build_payload(kw_list=br[i])
                dft = trend.interest_over_time()
                dft = dft.drop("isPartial", axis=1)
            #     print("DFT=\n",dft)
                if i == 0:
                    df = dft.copy()
                else:
                    df = pd.concat([df, dft], axis = 1)
            #     print("DF=\n",df)
                time.sleep(2)
                
            col = list(df.columns)

            pt = px.line(df, x=df.index, y = col)# ["Data Science", "Web Development", "Ethical Hacking", "Cybersecurity"])
            # pt.show()
            fig = plotly.offline.plot(pt, include_plotlyjs=True, output_type='div')

            return [fig, df]

        except Exception as e:
            return [f"<h1>An error was encountered. Error log: {e}</h1>", None]

def execute(text):
    ob = Trends()
    output = ob.getTrend(text)

    return output