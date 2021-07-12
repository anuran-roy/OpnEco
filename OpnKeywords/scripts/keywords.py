import pandas as pd
# import matplotlib.pyplot as plt
import re
# import seaborn as sns
import plotly.express as px
import plotly


class Keywords:
    keynum = 0
    def __init__(self, num):
        self.keynum = num

    def deEmojify(self, text):
        regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)

    def getKeywords(self, text):
        text = """{}""".format(text)
        text = text.replace(r"\n", " ")
        text = text.replace(r"\r", " ")
        text = self.deEmojify(text)
        text = text.replace("\n", " ")
        text = text.replace("\r", " ")
        symbols = '''@#$%^&*()_+-=|[]\:"';<>?,/—’”“:..! '''
        text = text.replace(symbols, " ")

        while "  " in text:
            text = text.replace("  ", " ")
        # print(r"{}".format(text))
        datadict={} #Dictionary for dataframe
        xlabels=[] #List for xlabels

        cwname=open("OpnKeywords/lists/google-10000-english-master/google-10000-english.txt","r")
        cwlist=[]
        with cwname as wfile:
            for wline in wfile:
                for cword in wline.split():
                    cword2=cword.lower()
                    cwlist.append(cword2)

        for word in text.split(" "):
            worde = self.deEmojify(word)
            wordf = worde.lower()
            word2 = wordf.strip(symbols)
            word2 = word2.rstrip(symbols)
            word2 = word2.lstrip(symbols)
            #print(word)
            if not word2.isnumeric() and word2 not in list(symbols): # and not (bool(re.match('^[a-zA-Z0-9]*$', word2))):
                if word2 in datadict:
                    datadict[word2]+=1
                elif word2 not in cwlist:
                    datadict[word2]=1
                    xlabels.append(word2)
        
        res = {key: val for key, val in sorted(datadict.items(), key = lambda ele: ele[1], reverse = True)} 
        df=pd.DataFrame.from_dict([res])
        df.describe()
        col=df.columns
        df=df.transpose()
        headd=df.head(self.keynum) if self.keynum < len(df) else df

        if self.keynum == 0:
            headd = df

        pt = px.line(headd)
        pt.update_layout({
            'plot_bgcolor': 'rgba(51, 51, 51, 1)',
            'paper_bgcolor': 'rgba(51, 51, 51, 1)',
            }, showlegend=False, font_color="white",title={
                'text': 'Suggested Keywords (sorted by frequency in decreasing order)',
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            })
        pt.update_traces(line_color='#04aa6d')
        fig = plotly.offline.plot(pt, include_plotlyjs=True, output_type='div')

        return fig

def execute(kn, text):
    ob = Keywords(kn)
    op = ob.getKeywords(text)

    return op
