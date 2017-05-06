'''
Created on Feb 18, 2017

@author: uuisafresh
'''
from flask import *
from ES import *
import nltk
import types
import shelve
app = Flask(__name__)

global search_results,cur_page,page_len
global dict_index, dict_json, result_index
global stop_dict


@app.route("/detail", methods=['POST'])
def go_detail():
    global search_results,cur_page,page_len
    select = request.form['inputDetail']

    #print select,(int(select)%page_len)
    return render_template("detail.html", result=search_results[int(select)-1],recommend=search_results[(int(select)%page_len)])
@app.route("/detail1", methods=['POST'])
def go_recommend():
    global search_results,cur_page,page_len
    select=request.form['RecomendPage']
    return render_template("detail.html", result=search_results[int(select)-1],recommend=search_results[(int(select))%page_len])


@app.route("/")
def search():
    return render_template('index.html')

@app.route("/results", methods=['POST'])
def results():
    global search_results,cur_page,page_len,stop_dict
#     try:
    query = request.form['inputValue']
    #print query, starring, genre
    #print query
    search_results, page_len = es_query(query)
    #print length
    cur=cur_page
    stop=[]
    stop_flag=False
    unknown=[]
    unknown_flag=False
    for q in query.split():
        dbq=nltk.PorterStemmer().stem(q).encode('utf8')
        if dbq in stop_dict:
            stop_flag=True
            stop.append(q)
    page=[i for i in range(len(search_results)//10)]
    return render_template('index.html',result=search_results[cur*10:(cur+1)*10], result_num=page_len, result_page=page[cur*10:(cur+1)*10], cur=cur, stop_flag=stop_flag,stop_word=stop,unknown_flag=unknown_flag, unknown=unknown)
#     except KeyError:
#         return '"Problem"'
    
@app.route("/jump_prev", methods=['POST'])
def jump_prev():
    #print "yes"
    global search_results,cur_page,page_len
    cur_page-=1
    cur_page=max(0,cur_page)
    cur=cur_page
    page=[i for i in range(len(search_results)//10)]
    #print cur_page,"prev"
    return render_template('index.html', result=search_results[cur*10:(cur+1)*10], result_num=len(search_results), result_page=page, cur=cur)
    
@app.route("/jump_next", methods=['POST'])
def jump_next():
    #print "yes"
    global search_results,cur_page,page_len
    cur_page+=1
    cur_page=min(page_len-1,cur_page)
    cur=cur_page
    #print cur_page,"next"
    page=[i for i in range(len(search_results)//10)]
    return render_template('index.html', result=search_results[cur*10:(cur+1)*10], result_num=len(search_results), result_page=page, cur=cur)
    

if __name__ == '__main__':
    cur_page=0
    stop_word="a the about above after again against all an and any as at be because before below between both but by cannot could did do down during each few for from further have here he how i if in into it itself let me more he it you most must my myself no nor not of off on once only or other ought our osu . ! ? , ;".split()
    global stop_dict
    stop_dict=dict()
    for s in stop_word:
        stop_dict[s]=1
    app.debug = True  
    app.run()
