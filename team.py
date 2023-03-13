import pandas as pd
import numpy as np
import random

df = pd.read_csv('Pokemon.csv')

#print(df.head())
#print(df[['Name']].to_string(index = False))

#have user choose pokemon type and display team for that

col_list = df.Name.values.tolist()
print(col_list)
TEAM_MEMBERS = 6

def main():
    while True:
        print("Enter how many team combinations you would like: ")
        combinations = input("> ")
        
        if not combinations.isdecimal():
            print('Please enter a digit.')
        else:
            numberOfTeams = int(combinations)
            break
        
    for i in range(numberOfTeams):
        for i in range(0, TEAM_MEMBERS):
            team = random.choice(col_list)
            team1 = random.choice(col_list)
            team2 = random.choice(col_list)
            team3 = random.choice(col_list)
            team4 = random.choice(col_list)
            team5 = random.choice(col_list)


            print(team + ", " + team1 + ", " + team2 + ", " + team3 + ", " + team4 + ", " + team5) 
        
        
        
if __name__ == "__main__":
    main()