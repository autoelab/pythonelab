# pythonelab

Automagically solve all questions in your python elab.

## How do I use it?

- Download the latest executable from the [Release](https://github.com/pythonelab/pythonelab/releases) tab of this repo.
- Run it. That's it. Even a monkey could do it.

## Oh you want patch notes? Here:

- There are just two inputs now: Username and Password. I hope nobody would mess that up.
- Delay option is removed because who cares? I bet no one ever used it.
- This script will generate reports whether you want it to or not.
- It doesn't care if you already solved a question. It will overwrite your solution either way.

## Feel like reading more? Here:

- The major change in the login system was that every request now went through an api instead of a simple post request. That was easy to fix with some tweaks to the post request.

- What I failed to notice was that the data was being passed as a string instead of a dictionary. I was banging my head on the walls for days until a friend helped me figure that one out!

- Then I noticed the numbering pattern was changed. Thanks some more help, I was able to crack that too. The rest was relatively easier. It now returns the question id in the response so the search function wasn't needed anymore.

- It still uses the same solutions that are hosted on autoelab's repo which is why I didn't feel the need to upload them again here.

- Eventually I decided to re-structure the code and made it just one simple script instead of dividing it in functions, because why not? It's less than 36 lines of code. [Check it out](https://github.com/pythonelab/pythonelab/blob/master/pythonelab.py).

- I didn't wanna put too much work into it since all people really care about is that it gets the job done. Which is why I didn't bother to add any error handling. I mean, what could go wrong? amirite lads? haha..ha.. (i hope i dont regret this)

### FAQ, memes and warnings are the same as that on [autoelab](https://github.com/autoelab/autoelab)'s repo.
