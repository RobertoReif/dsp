# The football.csv file contains the results from the English Premier League.
# The columns labeled "Goals" and "Goals Allowed" contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in "for" and "against" goals.

import csv

def read_data(filename):
  goals = {}
  with open(filename,'rb') as f:
    reader = csv.reader(f)
    headers = reader.next()

    difference = 1000000
    for row in reader:
        team, goal, allowed = row[0], int(row[5]),int(row[6])
        if abs(goal-allowed)<difference:
            difference = abs(goal - allowed)
            team_val = team
        print (team_val)

goals = read_data('football.csv')

