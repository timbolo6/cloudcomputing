from flask import Flask
import json
from collections import Counter
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello Celery! Look at \count and wait 1 minute</p>"

@app.route("/count")
def count_pronouns():
    # Celery task
    from proj.tasks import count_pronouns_for1JSON
    queuedTask =[]
    results = {}
    input_path = "./data/05cb5036-2170-401b-947d-68f9191b21c6"
    #input_path = 'untitled.txt'
    with open(input_path) as file:
        for jsonObject in file:
            if not jsonObject.isspace():
                json_tweet = json.loads(jsonObject)  
                if (json_tweet['retweeted'] == False): 
                    text = json_tweet['text'].lower()
                    queuedTask.append(count_pronouns_for1JSON.delay(text))

    results = queuedTask[0].get()
    for i in range(1,len(queuedTask)):
        results = Counter(results) + Counter(queuedTask[i].get())

    return results
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5100,debug=True)
