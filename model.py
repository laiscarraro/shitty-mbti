import sklearn
import pickle
import pandas as pd
import random
import warnings
warnings.filterwarnings('ignore')

compliments = [
    "You look beautiful today!",
    "You have the most beautiful smile I've ever seen!",
    "Your intelligence is beyond human comprehension!",
    "You light up my day!",
    "You can do anything!",
    "Everyone loves you!",
    "I hope you're having the best day of your life!"
]

model = pickle.load(open('shitty-mbit/mbti.sav', 'rb'))
print('Thank you for waiting! ' + random.sample(compliments, k=1)[0] + ' 💚')
labels = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']

def get_my_mbti_already_you_btch(texto):
    t = ''
    results = {l: [] for l in labels}
    texts = []

    for c in texto.split(' '):
        t += ' ' + c
        texts.append(t)
        pred = zip(labels, model.predict_proba(pd.DataFrame([t], columns=['posts'])['posts'])[0])
        for p in pred:
            results[p[0]].append(p[1])

    df = pd.DataFrame(results)
    print('You are probably an... ' + labels[df.iloc[-1].argmax()] + '!!!')
    print('Here are the probabilities for each class:')
    for i in list(zip(labels, df.iloc[-1].values)):
        end = ''
        if i[0] == labels[df.iloc[-1].argmax()]: end = ' (this is you!)'
        print(i[0] + ': ' + str(round(i[1]*100, 2))+'%' + end)
    print('And here are the probabilities along the sentence:')

    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    fig, ax= plt.subplots(figsize=(15,8))
    f = ax.plot(df)
    ax.legend(f, labels)
    return fig
