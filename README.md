# electionresults
Quick and dirty lab exercise

Very quickly thrown together for a lab exercise. This python project requires python3 and flask to run this 'api server'

Due to time constraints I was unable to get the state/overall results implemented. I believe I have all the data required and the logic nearly in place BUT I wanted to stick to the two hour window.

Given more time I would have like to either figure out a way to clean tthe sample data provided to make it easier to read and manipulate. Also if I wouldn't have hit the time limit I would have like to have kept playing with pandas in python (which I'll probably do in my free time) as I think it would have made the data manipulation easier/cleaner

To Run:

python3 electionresults.py

Then in a webbrowser or curl verify http://127.0.0.1:5000/api/v1/resources/CountyWinners returns results. ( /StateWinners and /OverallWinners will return a 200 but they are currently just place holders)
