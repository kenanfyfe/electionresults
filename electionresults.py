import json
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Read the given json file
with open('electiondata.json') as json_file:
    data = json.load(json_file)
 

states=[]
votes_dic = {}
votes_county_canidate = {}
votes_county_canidate_party = {}
dem_can_by_county = {}
rep_can_by_county = {}
num_votes_dem = 0
num_votes_rep = 0
dem_winner = " "
rep_winner = " "

county_dem_winners=[]
county_rep_winners=[]
overall_primary_winners=[]
display_winner_by_county_rep=''
display_winnber_by_county_dem=''
#States
for i in data:
    #print(i)
    states.append(i)

for i in states:
    #print(data[i])
    votes_dic = data[i]

for key in votes_dic: #Get all the votes for each canidate in each party
    votes_county_canidate = votes_dic[key] # Store the county and Votes for each candiate in each party
    for ckey in votes_county_canidate:
        if ckey =='Democrats':
           dem_can_by_county = votes_county_canidate[ckey]
        if ckey =='Republicans':
           rep_can_by_county = votes_county_canidate[ckey]
        for dkey in dem_can_by_county:
           if dem_can_by_county[dkey] > num_votes_dem:
              num_votes_dem = dem_can_by_county[dkey]
              dem_winner = dkey
        for rkey in rep_can_by_county:
          if rep_can_by_county[rkey] > num_votes_rep:
             num_votes_rep = rep_can_by_county[rkey]
             rep_winner = rkey

    display_winner_by_county_rep="Republican Primary Winner for " + key + ' county ' + rep_winner
    county_rep_winners.append(rep_winner)
    display_winner_by_county_dem="Democratic Primary Winner for " + key + ' county ' + dem_winner
    county_dem_winners.append(dem_winner)

@app.route('/api/v1/resources/CountyWinners', methods=['GET'])
def api_all():
    return (display_winner_by_county_rep + ' ' + display_winner_by_county_dem)

@app.route('/api/v1/resources/StateWinners', methods=['GET'])
def api_all2():
    return ("place holder")
@app.route('/api/v1/resources/OverallWinners', methods=['GET'])
def api_all3():
    return ("place holder")




app.run()
