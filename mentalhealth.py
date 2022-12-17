import pandas as pd
import random
patterns=[]
responses=[]
data=pd.read_json('intents.json')
print(data.columns)
print(data.describe())
print(data.info())
print(data.dtypes)
print(data.memory_usage())
while True:
    for keys,values in data.items():
        for i,y in values.items():
            patterns.append(y['patterns'])
            responses.append(y['responses'])
    q="What's the difference between sadness and depression?"
    inp=input('-> ').capitalize()
    for i in range(80):
        if inp in patterns[i] :
            if len(responses[i][:-1]) > 1:
                print(random.choice(responses[i][:-1]))
            print(responses[i][-1])