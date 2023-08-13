#!/bin/bash

TEAM_VALUE=1
#echo "Owner,Player,Team,Position%n"

until [ $TEAM_VALUE -ge 15 ]
  do
    echo "Team value is $TEAM_VALUE"
    jq ".TEAM=$TEAM_VALUE" config.json > temp.json
    mv temp.json config.json
    npm start run
    python3 get_roster_from_json.py $TEAM_VALUE >> teamData/rosters.csv
    let "TEAM_VALUE+=1"
  done