from .celery import app
import re
from collections import Counter

@app.task
def addDict(x, y):
    return dict(Counter(x) + Counter(y))


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def count_pronouns(tweet_texts):
    hen_patter = re.compile("[^a-z]hen[^a-z]")
    han_patter = re.compile("[^a-z]han[^a-z]")
    hon_patter = re.compile("[^a-z]hon[^a-z]")
    den_patter = re.compile("[^a-z]den[^a-z]")
    det_patter = re.compile("[^a-z]det[^a-z]")
    denna_patter = re.compile("[^a-z]denna[^a-z]")
    denne_patter = re.compile("[^a-z]denne[^a-z]")
    counters = {'hen':0,'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0}
    # Loop through all tweets texts and count the pronouns
    for index, line in tweet_texts.items():
         # Hen Patter     
        if hen_patter.search(line):
            counters['hen'] += 1
        # “han” Patter       
        if han_patter.search(line):
            counters['han'] += 1
        # HON        
        if hon_patter.search(line):
             counters['hon'] += 1
               # DET        
        if den_patter.search(line):
            counters['den'] += 1
            # DET        
        if det_patter.search(line):
             counters['det'] += 1
        # DENNA        
        if denna_patter.search(line):
             counters['denna'] += 1
        # DENNE       
        if denne_patter.search(line):
            counters['denne'] += 1
    return counters


@app.task
def count_pronouns_for1JSON(one_tweet_text):
    hen_patter = re.compile("[^a-z]hen[^a-z]")
    han_patter = re.compile("[^a-z]han[^a-z]")
    hon_patter = re.compile("[^a-z]hon[^a-z]")
    den_patter = re.compile("[^a-z]den[^a-z]")
    det_patter = re.compile("[^a-z]det[^a-z]")
    denna_patter = re.compile("[^a-z]denna[^a-z]")
    denne_patter = re.compile("[^a-z]denne[^a-z]")
    counters = {'hen':0,'han':0,'hon':0,'den':0,'det':0,'denna':0,'denne':0}
    # Loop through all tweets texts and count the pronouns
       # Hen Patter     
    if hen_patter.search(one_tweet_text):
        counters['hen'] += 1
    # “han” Patter       
    if han_patter.search(one_tweet_text):
        counters['han'] += 1
    # HON        
    if hon_patter.search(one_tweet_text):
         counters['hon'] += 1
           # DET        
    if den_patter.search(one_tweet_text):
        counters['den'] += 1
        # DET        
    if det_patter.search(one_tweet_text):
         counters['det'] += 1
    # DENNA        
    if denna_patter.search(one_tweet_text):
         counters['denna'] += 1
    # DENNE       
    if denne_patter.search(one_tweet_text):
        counters['denne'] += 1
    return counters
