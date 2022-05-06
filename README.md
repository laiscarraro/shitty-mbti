# MBTI, but worse!
Shitty MBTI NLP model made with pyscript just for fun. Check out the ["""""web app"""""](https://laiscarraro.github.io/shitty-mbti/) if you haven't already!

The model was trained using [this kaggle dataset](https://www.kaggle.com/datasets/datasnaek/mbti-type) and a Logistic Regression model implemented with sklearn. I used a tf-idf vectorizer to extract the features and then selected the 10k best. I wasn't mentally prepared enough for hyperparameter tuning, so I basically used just the default ones. In the future, I might put the notebook here, too.

Then, I saved the model in a .sav file with the pickle lib, uploaded it to this repo and just accessed it in the pyscript in the html file. Pretty **n e a t**, am I right?

## Problems I faced in this example project

The tricky part of the "deployment", for me, was getting the paths right.

In the html file, if you look at the py-env setup you'll find the name of the libs I use, but also a "paths" part. When you're working locally, paths like "/filename" will work (also, quick tip: if you're working locally, you'll only be able to access other files in your html if you're using a web server, like Web Server for Chrome). 

When you upload it to pages, though, the link github creates has the repo name. So, when you're writing the paths in your py-env, don't forget to add the repo name in front of every path. In this case, it's "/shitty-mbti/filename", you can [check it out](https://github.com/laiscarraro/shitty-mbti/blob/main/index.html) if you don't believe me.

## Changes that would make this better

My webdev skills were a little rusty ~~and I just couldn't care less tbh~~ to make this a little better when I was developing the first "version", so here are some changes that might improve it:

**For the model part:**
- Training the model with better data (literally just doing a little preprocessing might already improve it)
- Testing different approaches (e.g.: bow instead of tf-idf, embeddings instead of those, ngrams, etc.)
- Playing with the hyperparameters

**For the "web app" part:**
- Doing some asynch stuff or at least making a progess bar to indicate the model is loading (instead of the green heart, although I still think it's cute af)
- Finding a better way to collect user input instead of literally creating a repl and letting them **code** (that was pretty bad, I own it, but c'mon I was tired)
- Fixing those horrendous `<br>`s with a little bit of css (or even just using bootstrap correctly would fix it)

If the idea of making any of these changes remotely interests you, I encourage you to fork this repo and give it a go. I'd love to see the shitty MBTI spread out its wings and fly.
