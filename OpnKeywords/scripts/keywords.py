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
        text = text.replace(r"\r\n", " ")
        datadict={} #Dictionary for dataframe
        xlabels=[] #List for xlabels

        cwname=open("OpnKeywords/lists/google-10000-english-master/google-10000-english.txt","r")
        cwlist=[]
        with cwname as wfile:
            for wline in wfile:
                for cword in wline.split():
                    cword2=cword.lower()
                    cwlist.append(cword2)
        
        symbols='!@#$%^&*()_+-={}|[]\:";<>?,./'
        
        for word in text.split(" "):
            worde=self.deEmojify(word)
            wordf=worde.lower()
            word2=wordf.strip(symbols)
            #print(word)
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

        fig = px.line(headd)

        graph_div = plotly.offline.plot(fig, include_plotlyjs=True, output_type='div')

        return graph_div

def execute(kn, text):
    ob = Keywords(kn)
    op = ob.getKeywords(text)

    return op
