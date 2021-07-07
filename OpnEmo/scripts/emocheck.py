#!/usr/bin/env python
# coding: utf-8

# ## Taking filename as input and reading data from it
# ## Importing necessary tools

import nltk
nltk.download('movie_reviews')
from textblob import TextBlob as tb
from textblob.sentiments import NaiveBayesAnalyzer
import plotly.express as px
import plotly
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import text2emotion as te
import os
# import glob
# import io
# import base64
# from base64 import decode

class Checker:
    #txtpath=input("Enter location of text file to read:")
    #fopen=open(txtpath,"r")
    def check(self, t):
        
        t = t.replace(r"\r\n", "\n")
        text = t
        # print("Setup complete")

        #l=len(t)

        #for i in range(l):
        #    for word in t[i].words:
        #        print (word)

        #np=s.noun_phrases
        #print(np)


        # ## Using NaiveBayesAnalyzer of TextBlob to determine the tone (positivity or negativity) in sentences
        # files = glob.glob('emotionchecker/generated/images/*')
        # for f in files:
        #     os.remove(f)
        s=tb(text,analyzer=NaiveBayesAnalyzer())
        sc=s.sentiment
        #print(sc)
        #print(s.sentences)
        t=s.sentences
        type(t)
        #print(t)
        avg=0
        spos=[]
        sneg=[]
        ssen=[]
        for sen in t:
            avg+=(sen.sentiment.p_pos-sen.sentiment.p_neg)
            
        avg/=(2*len(t))
        avg+=(sc.p_pos-sc.p_neg)/2

        sent=[]

        sen=t[0]
        senc=range(1,len(t)+1)
        
        for sen in t:
            sent.append(sen.sentiment.p_pos-sen.sentiment.p_neg)

        # pt=sns.scatterplot(y=sent,x=senc)
        # pt.set(ylabel='Emotion score',xlabel='Sentence number')

        pt1 = px.scatter(x = senc, y = sent, labels={
            "x": "Sentence number",
            "y": "emotion score"
        })

        fig1 = plotly.offline.plot(pt1, include_plotlyjs=True, output_type='div')        

        # pt1=sns.lineplot(y=sent,x=senc)
        # pt1.set(ylabel='Emotion score',xlabel='Sentence number')

        pt2 = px.line(x = senc, y = sent, labels={
            "x": "Sentence number",
            "y": "emotion score"
        })

        fig2 = plotly.offline.plot(pt2, include_plotlyjs=True, output_type='div')        

        # ## Determining the opinion and polarity of the sentences using rules based matching with TextBlob

        s2=tb(text)
        pol=s2.sentiment.polarity
        sub=s2.sentiment.subjectivity
        t2=s2.sentences
        spol=[]
        ssub=[]
        for sen2 in t2:
            spol.append(sen2.sentiment.polarity)
            ssub.append(sen2.sentiment.subjectivity)

        avgp=sum(spol)/len(spol)
        avgs= sum(ssub)/len(ssub)

        # print(avgp)
        # print(avgs)

        cpos=0
        cneg=0

        for i in ssen:
            if i=='pos':
                cpos+=1
            elif i=='neg':  
                cneg+=1
        # print(f"Positive sentences detected = {cpos}")
        # print(f"Negative sentences detected = {cneg}")
        #sns.barplot(data={'positive':cpos,'negative':cneg})        

        emodict=te.get_emotion(text)

        # print(emodict)
        emodict['Tone']=avg
        keys=list(emodict.keys())
        vals=[100*float(x) for x in list(emodict.values())]

        pt3 = px.bar(x = keys, y = vals, labels={
            "x": "<-------Emotion------->",
            "y": "Percentage----->"
        })


        fig3 = plotly.offline.plot(pt3, include_plotlyjs=True, output_type='div')        

        s = """{\n"""
        for i in list(emodict.keys()):
            if i != list(emodict.keys())[-1]: 
                s += f"'{i}': {round(emodict[i],4)*100}%\n"
        s += f"'Tone': {round(emodict['Tone'],4)*100}%\n"
        s += "}"
        
        return [s, fig1, fig2, fig3]

def execute(toAnalyze):
    ob = Checker()
    # print(os.path.basename(__file__))
    score = ob.check(toAnalyze)
    # s = ""
    # for i in list(score.keys()):
    #     if i != list(score.keys())[-1]:
    #         s += f"{i}: score[i] , "
    #     else:
    #         s += f"{i}: score[i] "
    
    # return s
    return score

if __name__ == '__main__':
    a = execute("Hello there! I am Anuran! How do you do?")