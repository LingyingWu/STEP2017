# Description of programs
Implement a basic othello agent using __Google App Engine__.  
[This page](https://github.com/LingyingWu/hw7) includes details and initial templates of the programs.  

Links:
- Othello game URL: [https://step-reversi.appspot.com](https://step-reversi.appspot.com)    
- Source code of the agent: [othello-lynn.py](https://github.com/LingyingWu/STEP2017/blob/master/week7/othello-lynn.py)  
- Application URL of the agent: [https://othello-lynn.appspot.com](https://othello-lynn.appspot.com)

***
## Using reflector.go

You can use this "reflector" program to make a locally running dev_appserver instance act like a human player (i.e. you don't have to deploy the whole app to have it run a game).

To run it:
* [download](https://golang.org/dl/) and install Go if you don't have it already.
* Start a new game on https://step-reversi.appspot.com with a "Human (or Local bot)" selected as one of the players
* copy the URL of that browser tab showing that game (i.e. a URL that looks like "https://step-reversi.appspot.com/view?gamekey=fOoBaR")
* type `go run reflector.go "https://step-reversi.appspot.com/view?gamekey=fOoBaR"`
    * (but pasting your actual viewer URL there -- fOoBaR is not a real game ;)
